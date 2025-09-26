+++
title = "Cake"
authors = ["damien-maier"]
date = 2023-11-04

[taxonomies]
categories = ["pwn"]
+++

I am the author of this challenge. This MD contains some information about the chall and a detailed explanation of how I expected players to solve it.

## Challenge design

This challenge is run differently than the usual pwn challenges. Pwn challenges often consist of a program that reads and writes stuff to stdin/stdout. The challenge server will wait for TCP connections and, for each TCP connection, it executes the program in a new process with stdin/stdout connected to the client socket.

This challenge is different. Here the program itself is the server. It waits for TCP connections in an infinite loop and, when a connection occurs, it forks itself and the child process is responsible for communicating with the client. We will see that this specific design increases the vulnerability of the server.

You may wonder what the purpose of those lines of code is (at the beginning of the `welcome` function) :

```c
int a = rand();
int b = rand();
int c = rand();
int d = rand();
int e = rand();

unsigned int subject_number = (unsigned int) (a+b+c+d+e) % 1000;

char subject_number_string[100];
snprintf(subject_number_string, 100, "%d", subject_number);
```

Actually this is just a way to force the compiler to use more registers for this function, which is necessary for the binary to include an ROP gadget needed for the attack.

The program is compiled with a modern gcc and without disabling any security. The only compilation flag is `-O3` to enable optimisations. Yet we will see that we are able to bypass all mitigations and get a remote shell.

## The buffer overflow

The vulnerability is inside the `authenticate` function, right at the top of the source file.

```c
char password[100] = {};

char *password_pointer = password;
char input_char;

while(1){
    ssize_t read_return = read(file_descriptor, &input_char, 1);
    if (read_return <= 0 || input_char == '\n') {
        break;
    }
    *password_pointer = input_char;
    password_pointer++;
}
```

This code will read data from the socket byte by byte, in an infinite loop, and write it in the `password` buffer. We only exit the loop when a `\n` is received (or if the socket is closed), there is nothing that checks that the received data fits inside `password`. Thus, we can do a buffer overflow on the stack.

However, as the modern mitigations are present, this is not trivial to exploit. We will face the following obstacles :

- The stack canary is here to prevent us from overwriting the return address of the function
- Even if we manage to bypass the canary, ASLR is enabled and the program is PIE, so we have no idea what to write at the return address location
- Even if we bypass ASLR, the stack is not executable and, more generally, all the executable areas of the process memory are read only

Let see how to bypass all of this and get a shell.

## The stack layout

To understand what we are overwriting when we trigger the overflow, let's attach gdb to the process and draw the interesting part of the stack.

Each line is 8 bytes. The small addresses are at the top, the big addresses are at the bottom.

| name                   | value                                                   |
| ---------------------- | ------------------------------------------------------- |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| password buffer        |                                                         |
| canary                 | random                                                  |
|                        |                                                         |
| socket file descriptor | 4                                                       |
|                        |                                                         |
|                        |                                                         |
|                        |                                                         |
| return address         | main+451 (main is at a random location because of ASLR) |


We can see that the compiler inlined the `authenticate` function inside the `welcome` function. This explains the fact that the return address goes back directly to `main`.

Notice the `4` value stored in the stack between the canary and the return address. To be honest I don't know exactly why it is there, but this is where the `main` function stores the file descriptor for the client socket. When we overflow, we will need to preserve this value because otherwise the `main` function will not correctly send the final "still alive..." message. We will see that this is important.


## Bypassing the canary

The particular server design that I have described above allows us to attack the canary.

In classical pwn challenges, a new instance of the program is run for each TCP connection, with the `fork exec` system call. `exec` triggers the initialization of a new process and the choice of new random values for the canary and ASLR. Thus, each time a player connects to the challenge, the process to attack has different random canary and ASLR values.

In this challenge, a new process is `fork`ed for each TCP connection, but there is no `exec` as the server itself contains the code to serve clients. When a `fork` happens, the child process inherits the ASLR layout and the canary value from the parent process. This means that, each time we connect to the challenge, the canary value and ASLR layout will be the same ! (It will only change if the CTF admins restart the challenge).

Although the canary does not change from connection to connection, we still don't know its value. A direct bruteforce is not feasible because the canary is a very large number. The solution ? Brute force byte by byte !

Let say that we want to know the first byte (the low byte) of the canary. We send an overflow that will fill the stack until right before the canary, then we send our guess for the first canary byte.

If our guess is wrong, the canary change will be noticed right before the `welcome` function returns, and the process will crash. (Notice that we are talking about the child process here, the parent process is not affected and will happily accept subsequent connections). In this case, we will not receive the final "still alive..." message, because it is sent from the `main` function, after the return of `welcome`.

If our guess is correct, we will know it because the program will execute normally and we will receive the "still alive..." message.

After having discovered the first canary byte, when can continue with the second, the third, etc. until we know it entirely.

Note that if one of the canary byte happens to be `0x0a` (ASCII code for "\n"), then it is impossible to continue the overflow after this value. This is because the vulnerable loop that performs the overflow exits when it encounters a `\n`. This situation is however quite unlikely.

The canary is 8 bytes long but its low byte is always 0, so we actually have 7 bytes to guess. With an average 128 number of try per byte, this is 7 * 128 = 896 connections in average, which is feasible in less than two minutes (at least when I run the challenge on my computer).

## Defeat ASLR of the executable

Now that we know the canary, we can use the same bruteforce technique to discover the return address value, byte by byte. If we overwrite the return address with an incorrect value, the program crashes when it returns from `welcome`. Otherwise, it continues correctly and we receive the final message.

For this, our payload will be `data to fill the password buffer` + `canary` + `data to reach the return address` + `data that partially overflows the return address`.

Beware that, as explained above, we need to make sure that the data that fills the space between the canary and the return address has a `4` value at the right location, because otherwise we never receive the "still alive..." message from `main`.

Another thing to take into account is that if we bruteforce the first byte (the low byte) of the return address, there are a lot of values that wont result in a crash but instead will make us jump in some random location into or near the `main` function. Because the low byte of the return address is not affected by ASLR (the random offset for the binary location in memory is a multiple of 0x1000), we can just check its value in GDB and use it directly.

So the return address is a pointer, thus 8 bytes long, but we already know the low byte. Also the 2 high bytes are always 0. So this is a 5 bytes bruteforce, 5 * 128 = 640 connections on average.

Now that we know the return address, we can compute the address of the `main` function, because we know from the stack layout above that the return address is main+451. Even though the position of the functions is randomized because of ASLR, the relative offsets between the functions of the program stay constant. Thus, now we know the address of every function of the executable.

With this knowledge, we can do ROP using gadgets found in the executable.

## Defeat ASLR of Libc

As the program is very small, it does not provide a lot of interesting ROP gadgets. The next step for us is to find the address of the `libc` file in memory, which contains everything we need to get a shell.

The offset of libc and the offset of the program are two random values that are generated independently, so we can not compute the address of `libc` from the address of the program.

To get the address of `libc`, we will do ROP to call the `write` function in order to send us a libc pointer through the socket. The `write` function takes three arguments (as this is a 64 bits program, they are passed through registers) :

- The file descriptor were the data should be written, in `rdi`. We want so set it to the file descriptor for the client socket, which is 4.
- A pointer to the first byte of the data that will be sent, in `rsi`. We want to set it to the address of a pointer that points to something in libc.
- The number of bytes to send, in `rdx`. We want to set it to any value larger or equal to 8.

Luckily, when we reach the return of `welcome` and start the ROP execution, `rdi` already contains the value 4, and `rdx` contains a value higher than 8. This is due to the fact that the last function call before the return of `welcome` is the call to `write` for sending "You are not authorized to access the cake :(\n".

The executable contains a `pop rsi; ret` gadget that we can use to change the value of `rsi`. We will set it such that it points to some entry of the GOT (global offset table). The GOT is a data structure that is inside the memory region of the executable, so we know its address. It contains the addresses of the libc functions that the program uses. Let say we set `rsi` to the address of the GOT entry for the `puts` function.

We can now send our ROP chain that will call `write(4, <address of GOT entry for puts>, <some number higher than 8>)`. The first 8 bytes of what we get in return represent the address of the `puts` function in libc.

As we have access to the exact `libc` file used by the server (it is provided in the challenge files), we can now use the `puts` pointer to compute the base address of `libc` in memory, and thus we know the address in memory of everything that libc contains.

## Get a shell

Now that we know the address of `libc`, we can call any of its functions in our ROP chains. As `libc` contains a lot of gadgets, we can also freely change the argument register values before calling a function.

There is one last obstacle in our way. If we directly open a shell (by executing `system("/bin/sh")`), the shell will expect data from stdin and print output to stdout. Stdin and stdout are connected to the terminal of the server, so this will open a shell in the terminal of the computer that runs the challenge, which would be useless for us. We need a way to make the input / output of the shell go through the TCP socket to us.

The good news is that there exists a `libc` function that does exactly that : the function `dup2`. It takes two file descriptors as arguments, and makes the second file descriptor point to the file connected to the first file descriptor. Here the "file" is the TCP socket. The file descriptor for stdin is 0, the file descriptor for stdout is 1 and the file descriptor for the client socket is 4. So we want to call `dup2(4, 0)` and `dup2(4, 1)`, which will connect both stdin and stdout to the socket.

Finally, for calling `system("/bin/sh")` we need a pointer to a "/bin/sh" string. Very conveniently, `libc` contains this string, and because we can compute the address of everything inside `libc`, we know its address.

To recapitulate, we build a ROP chain that :

- Sets `rdi` to 4
- Sets `rsi` to 0
- Calls `dup2`
- Sets `rdi` to 4
- Sets `rdi` to 1
- Calls `dup2`
- Sets `rdi` to the address of the "/bin/sh" string in libc
- Calls `system`

And now we have a shell, where we can type `cat flag.txt` and get the flag in return !

## Note about the unlikely situation where the attack is infeasible

As explained in the part about the canary, if any byte of the canary is `0x0a`, the attack is infeasible. There is the same situation with the return address.

As the canary contains 7 random bytes and the random part of the return address is 5 bytes long, the probability for this to happen is 1  - (255/256)^12, which is around 5%. This is why it is important to test that the attack works and restart the server if it doesn't.
