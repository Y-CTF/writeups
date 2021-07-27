from pwn import *


#where is this place
r = remote("mc.ax", 31796);

answer = r.recvline();
print(answer.decode('utf-8'));

me = "add flour";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));


me = "add yeast";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "add salt";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "add water";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
answer = r.recvline();
answer = r.recvline();
print(answer.decode('utf-8'));


me = "hide the bowl inside a box";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));


me = "wait 3 hours";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));


me = "work in the basement";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));


me = "preheat the toaster oven";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "set a timer on your phone";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "watch the bread bake";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));



me = "pull the tray out with a towel";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "open the window";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));



me = "unplug the fire alarm";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "unplug the oven";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));



me = "wash the sink";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "clean the counters";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));




me = "flush the bread down the toilet";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));


me = "get ready to sleep";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));


me = "close the window";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));

me = "replace the fire alarm";
print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));


me = "brush teeth and go to bed";

print(me);
r.sendline(bytes(me, 'utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
answer = r.recvline();
print(answer.decode('utf-8'));
