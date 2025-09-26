+++
title = "X-RAY"
description = "The SOC detected malware on a host, but antivirus already quarantined it... can you still make sense of what it does? "
authors = ["glys"]
date = 2024-09-30

[taxonomies]
categories = ["malware", "reverse"]
+++

## Description

The SOC detected malware on a host, but antivirus already quarantined it... can you still make sense of what it does? 

----

```
   huntress file x-ray
x-ray: data
   huntress hexdump -C x-ray | head
00000000  0b ad 00 98 91 fd de 68  52 f9 91 c7 81 fa fc 90  |.......hR.......|
00000010  8a a2 ad b3 69 34 07 1c  02 61 bc c2 c0 e8 ca e7  |....i4...a......|
00000020  f1 ff a3 02 3e 58 32 b2  31 de ef e0 7c bc bb 0a  |....>X2.1...|...|
00000030  42 33 a0 21 c1 85 e5 28  21 ba 6d ea bc 8b 09 82  |B3.!...(!.m.....|
00000040  4a f9 f4 9f 9f 2d 78 20  f7 2f 8a 3a c6 85 74 ce  |J....-x ./.:..t.|
00000050  4b 21 f1 13 3e 79 72 58  a2 30 34 ca e2 11 8c 26  |K!..>yrX.04....&|
00000060  e2 ef 8f c4 5f 06 7c 56  70 7f c1 df 51 24 a0 29  |...._.|Vp...Q$.)|
00000070  50 66 4d c7 7d f4 32 f0  f7 da cf 12 8a 73 89 d3  |PfM.}.2......s..|
00000080  da 36 ee 6c b0 cf 99 e1  eb 2c 70 86 ad b0 c3 3a  |.6.l.....,p....:|
00000090  99 ce 98 f2 72 ff 5e 28  53 bd 59 81 c8 1c 5e f8  |....r.^(S.Y...^.|
```

High entropy, this looks encrypted.

After trying to decode it using PE or ELF header as a crib for xor, no success, I tried looking for antivirus quarantine on google.
I found this: https://github.com/knez/defender-dump/tree/master
Just needed to modify it slightly to decrypt my file.

Modified `defender-dump.py`
```python
...
if __name__ == '__main__':
    with open('x-ray', 'rb') as f:
        content, _ = unpack_malware(f)
    with open('x-ray.dec', 'wb') as f:
        f.write(content)
```

```
   huntress python3 defender-dump/defender-dump.py
   huntress file x-ray.dec
x-ray.dec: PE32 executable (DLL) (console) Intel 80386 Mono/.Net assembly, for MS Windows, 3 sections
```

Loading at this in Binary Ninja or IDA doesnt give good results.
Looking at strings does though.

```
   huntress strings x-ray.dec
...
.NET Framework 4.8
...
C:\Users\johnh\Source\Repos\pwncat-windows-c2\stagetwo\obj\Release\stagetwo.pdb
...
```

I found this
https://github.com/calebstewart/pwncat-windows-c2

which is a dll (.NET C#) implementation of pwncat-c2
(ofcourse we see it in strings too)

Loading it in ILSpy we find 2 methods that are not present in the github version:

![](https://i.imgur.com/6W91oFi.png)

This is just a simple xor

![](https://i.imgur.com/uB051qu.png)


