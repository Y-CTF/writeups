+++
title = "Strive Marish Leadman TypeCDR"
description = "Looks like primo hex garbage.\nMaybe something went wrong?\nCan you make sense of it? "
authors = ["glys"]
date = 2024-09-30

[taxonomies]
categories = ["crypto"]
+++

## Description

Looks like [primo hex garbage](https://www.ntietz.com/blog/rsa-deceptively-simple/).
Maybe something went wrong?
Can you make sense of it? 

----

Upon connecting to the service we get rsa values.
These are different on each connect.

```
   huntress nc challenge.ctf.games 30814
p: 0xc6eb6997016d204b540c1da50e5ff68b0ffaa565a3a8594e2f227f4d5b94070c27c16ce1d5d71ee4cca71b7931f02ad4d25f4e215c9f7588c247e996b93c80df
q: 0xc6b8954f39801616c9b450018a9618a3d60517e0a13e7f1705a698813be6bd77b50a38f74375009e7caca951e659f81915e31bb80edd0a5cd40379937fafd435
d: 0x44e781a1688bae70205dca67f6ac955f73572191b72ba02e14be2d9d7ac848c3c1f7ec3deb3ed855e67b6bec28815eef95a0611cd46407246a33068f3880591705332d0b16f9eedf49a7ba97db87211faf7ac1ee20c5534704dcb9a3f6c27c0140b0e002c5426838ac40239d16067b9da49f45e63c9b07ebe0d44563b640e6b9
e: 0x10001
n: 0x9a6980e3436bd838c879983ff22c8e707d8cb8fd3b4857d4d5cd0e96dd146697cb5ecffc24d78bb927be8b3b4ac735d59ead4224ef9ca8e103df7a677a2bb1d0267b1318a6ba5146bf8b9378bac242d1bae426c7f15eaa5aaf801e4caa405389d46d9ade2da4715570649e4781d1d2c83bd46286e75ebdea5f8638f22db05a2b

0x73b0be69adc7244a161074be4d3105ecbce644ce2c433bc470111fd9d2c3e5b59f7c8297871d62001b97f12d0fdd74ecef60b4c07d2d0f3f41963704ff806c5e3143df79ef093eb5a8d12e9fb86acef7a16cb243c8ed3954720c3b6d0e9107a864317799192e41dad077b042d6d0a58573485b9162a156a3e2b3e2b61ac5f13f
```

Decrypting the bottom number with a python script always gives
```
13040004482825409713878684097082783294385439409007049196036599611841074762489249861841795197
```

Following logicfrom article linked in challenge prompt we decode as bytes
```python
num = 13040004482825409713878684097082783294385439409007049196036599611841074762489249861841795197

msg = []
while num > 0:
    out = num % 256
    num = num // 256

    msg = [chr(out)] + msg

print(''.join(msg))
```


