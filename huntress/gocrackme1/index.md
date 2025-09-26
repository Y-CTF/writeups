+++
title = "GoCrackMe1"
description = "TENNNNNN-HUT!\n\nWelcome to the Go Dojo, gophers in training!\n\nGo malware is on the rise. So we need you to sharpen up those Go reverse engineering skills. We've written three simple CrackMe programs in Go to turn you into Go-binary reverse engineering ninjas!\n\nFirst up is the easiest of the three. Go get em! "
authors = ["glys"]
date = 2024-09-30

[taxonomies]
categories = ["reverse"]
+++

## Description

TENNNNNN-HUT!

Welcome to the Go Dojo, gophers in training!

Go malware is on the rise. So we need you to sharpen up those Go reverse engineering skills. We've written three simple CrackMe programs in Go to turn you into Go-binary reverse engineering ninjas!

First up is the easiest of the three. Go get em! 

----

As expected we get a Go binary:
```
   huntress file GoCrackMe1
GoCrackMe1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=XTzA9g-rxSFKyebZYVXI/BFzZeSPLsNjAFEvjiSub/nTgut0H_UB7B79xaGq7-/X7kvo6zmAQOjIJV9zPwd, with debug_info, not stripped
   huntress ./GoCrackMe1
Access Denied!
```

Nice, I did a bit of go reversing so this might actually be interesting.
Decompiling we find something looking like a one byte xor

```
00000000004836ad      for (int64_t i = 0; i < 0x26; i += 1)
00000000004836ad      {
00000000004836a0          n = ((uint64_t)(((uint32_t)*(uint8_t*)(&var_56 + i)) ^ 0x56));
00000000004836a3          *(uint8_t*)((char*)rax_1 + i) = n;
00000000004836ad      }
```

But there is also this line:`

```
00000000004836c8      rax_4 = main.checkCondition(~r0_1);    
```

So let's just breakpoint on this.

![](https://i.imgur.com/Na5ybxH.png)

Oh!
Well that is done I guess?

Next ones should be harder.
