+++
title = "Rustline"
description = "Jerry: A Redline Stealer.\nGeorge: Written in Rust.\nJerry: A Rusty Redline Stealer.\nGeorge: A Rusty Redline Stealer, Jerry!\n\nWe caught a Redline variant executing on an endpoint and intercepted the encrypted files as they traversed the edge proxy. Well, everything except for the flag.txt file (imagine that...). Any chance you could figure out how this thing works and recover the flag? NOTE: Archive password is rustline"
authors = ["cstef"]
date = 2024-09-30

[taxonomies]
categories = ["malware"]
+++

## Description

Jerry: A Redline Stealer.
George: Written in Rust.
Jerry: A Rusty Redline Stealer.
George: A Rusty Redline Stealer, Jerry!

We caught a Redline variant executing on an endpoint and intercepted the encrypted files as they traversed the edge proxy. Well, everything except for the flag.txt file (imagine that...). Any chance you could figure out how this thing works and recover the flag? NOTE: Archive password is rustline

----

We are given an executable that is presumably a malware. Running it under a VM and looking at the syscalls it makes with ProcMon, it looks like it's reading all the files in the `challenge-files` directory and tries to open a connection to `super-ultrasus.huntressctf.local`. This was later confirmed by a static analysis by finding this hostname again in the strings of the executable.

There were now two ways of solving this: reverse-engineering the encryption happening in the binary by decompiling it blah blah blah, or spoofing `super-ultrasus.huntressctf.local` by overriding `/etc/hosts` and trying to intercept what was sent. I went the latter because I was lazy and it seemed clearly simpler if we had a bit of the luck and the encryption wasn't too hard.

We first generate our good old `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` payload, put it in `challenge-files` and write a quick and dirty web-server to intercept:

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST', 'PUT', 'DELETE'])
def upload():
    filename = request.headers.get("x-filename")
    body = request.data
    if filename == "payload.txt":
        app.logger.info(f"Received request")
        with open("payload.txt.enc", "wb") as f:
            f.write(body)
    return "OK"


if __name__ == '__main__':
    app.run(debug=True, port=80)
```

`payload.txt.enc` looking pretty good !

```
0x0000010 F9 B6 6E B7 D4 19 36 04 F1 CE 9D CF A6 5B 9E 3F
0x0000020 F9 B6 6E B7 D4 19 36 04 F1 CE 9D CF A6 5B 9E 3F
```

The shift seems to repeat every 16 bytes, let's build a dictionnary!

```python
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?!()[]{}<>^'\"@#$%&+-=*/_\\|~` "
out = ""
for char in alphabet:
    out += char * 16
print(out)
```

We repeat the process to get our encrypted dictionnary and put it in our decryption script:

```python
REPEAT = 16
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?!()[]{}<>^'\"@#$%&+-=*/_\\|~` "

payload = open("payload.txt.enc", "rb").read()

mappings = {}

# Map all chars for indexes 0-15
for i in range(int(len(payload)/REPEAT)):
    chars = payload[i * REPEAT:(i + 1) * REPEAT]
    current_char = ALPHABET[i]
    mappings[current_char] = chars

to_decrypt = open("flag.txt.enc", "rb").read()

out = ""

for i in range(len(to_decrypt)):
    current_char = to_decrypt[i]
    # Find the corresponding encrypted char at the current index
    for key, mapping in mappings.items():
        if mapping[i % REPEAT] == current_char:
            out += key
            break
    

with open("flag.txt", "w") as f:
    f.write(out)
```

Run it:

```bash
python3 decrypt.py | grep "flag"
```

```
flag{bfe12aadd139def4d47f5f51a539249d}
```

Flagged !