+++
title = "GoCrackMe3"
description = "You've trained, you've failed, you've succeeded, you've learned. Everything you've done up to this point has prepared you for this moment. Don't let me down, Gopher. Don't let me down."
authors = ["cstef"]
date = 2024-09-30

[taxonomies]
categories = ["reverse"]
+++

## Description

You've trained, you've failed, you've succeeded, you've learned. Everything you've done up to this point has prepared you for this moment. Don't let me down, Gopher. Don't let me down.

----

For this 3rd and last edition of `GoCrackMe`s, we have a completely stripped binary. This makes the reversing task much harder than last time.

We start out by trying to figure out where the prints are located in the disassembled code:

```
cstef@debian-intel:/Users/cstef$ ./GoCrackMe3
Access Denied!
```

No raw strings are found inside the binary, so we'll try to go up the `syscall(write, ...)` to find the main function.
After ~~a lot~~ a bit of digging, we finally find something at `0x4f7a00`. The function contains many calls to the function at `0x4e5340`. Breaking at this function, we notice it is effectively the code responsible for printing "Access Denied!"

```c
0x4f7a00  int64_t real_main_this_time() {
0x4f7a0c      int64_t var_300;
0x4f7a0c      void* r14;
0x4f7a0c      
0x4f7a0c      if (&var_300 <= *(uint64_t*)((char*)r14 + 0x10))
0x4f7a0c      {
0x4f81b5          sub_4574a0();
0x4f81b5          /* no return */
0x4f7a0c      }
0x4f7a0c      
0x4f7a20      int64_t rax;
0x4f7a20      int64_t rbx;
0x4f7a20      rax = cQmrnwUU_LA_u_2d();
0x4f7a2a      int32_t rcx;
0x4f7a2a      
0x4f7a2a      if (!((TEST_BITQ(rax, 0x3f))))
0x4f7a46          rcx = rax;
0x4f7a2a      else
0x4f7a2a      {
0x4f7a2c          rcx = rax;
0x4f7a40          rbx = (((rax << 1) >> 0x1f) + 0xdd7b17f80);
0x4f7a2a      }
0x4f7a2a      
0x4f7a6a      XRFkNj_C_XuG5O5dqIkIw((-0x5e4dfc14c2e60000 + (((int64_t)(rcx & 0x3fffffff)) + (rbx * 0x3b9aca00))));
0x4f7a76      int128_t zmm15;
0x4f7a76      
0x4f7a76      if (sub_4f79a0() == 0)
0x4f7a76      {
0x4f7cc0          void* rax_10;
0x4f7cc0          int64_t rbx_4;
0x4f7cc0          rax_10 = sub_4f8500();
0x4f7cc5          int128_t var_50 = zmm15;
0x4f7cce          void* rax_11 = sub_409fe0(rax_10, rbx_4);
0x4f7cda          var_50 = &data_505400;
0x4f7ce2          *(uint64_t*)((char*)var_50)[8] = rax_11;
0x4f7d15          return access_denied(&data_543c58, data_5cd278, &var_50, 1);
0x4f7a76      }
// ...
0x4f7cb2      
0x4f7d34      for (int64_t i = 0; i < 5; i += 1)
0x4f7d34      {
0x4f7d4a          void* rcx_8 = *(uint64_t*)rax_9;
0x4f7d59          void* var_258_1 = *(uint128_t*)((char*)rax_9 + 8);
0x4f7d65          var_248 = *(uint128_t*)((char*)rax_9 + 0x18);
0x4f7d78          char rax_14;
0x4f7d78          rax_14 = *(uint64_t*)*(uint64_t*)((char*)var_248)[8]();
0x4f7d78          
0x4f7d82          if (rax_14 == 0)
0x4f7d82          {
0x4f7e45              void* rax_18;
0x4f7e45              int64_t rbx_9;
0x4f7e45              rax_18 = sub_4f92c0();
0x4f7e4a              int128_t var_228 = zmm15;
0x4f7e53              void* rax_19 = sub_409fe0(rax_18, rbx_9);
0x4f7e5f              var_228 = &data_505400;
0x4f7e67              *(uint64_t*)((char*)var_228)[8] = rax_19;
0x4f7e9a              return access_denied(&data_543c58, data_5cd278, &var_228, 1);
0x4f7d82          }
0x4f7d82          
0x4f7db2          void* rax_15 = sub_444800(&data_505480, var_258_1, var_258_1);
0x4f7db2          
0x4f81ae          for (int64_t j = 0; j < var_258_1; j += 1)
0x4f81a4              *(uint8_t*)((char*)rax_15 + j) = ((int8_t)!(((uint32_t)*(uint8_t*)((char*)rcx_8 + j))));
0x4f81a4          
0x4f7dd6          void* rax_16;
0x4f7dd6          int64_t rbx_8;
0x4f7dd6          rax_16 = sub_447ca0(0, rax_15, var_258_1);
0x4f7dfa          rbx_3 = &var_148;
0x4f7e02          void** rax_17;
0x4f7e02          int64_t rcx_13;
0x4f7e02          int64_t rsi_3;
0x4f7e02          rax_17 = sub_40ff20(&data_50bde0, rbx_3, var_248);
0x4f7e0f          rax_17[1] = rbx_8;
0x4f7e0f          
0x4f7e1a          if ((*(uint32_t*)data_62dd30) != 0)
0x4f7e1a          {
0x4f7e29              void** r11_1 = sub_459220(rax_17, rbx_3, rcx_13, rdi_2, rsi_3, r8, r9, r10);
0x4f7e2e              rsi = rax_16;
0x4f7e36              *(uint64_t*)r11_1 = rsi;
0x4f7e39              rdi_2 = *(uint64_t*)rax_17;
0x4f7e3c              r11_1[1] = rdi_2;
0x4f7e1a          }
0x4f7e1a          else
0x4f7e1c              rsi = rax_16;
0x4f7e1c          
0x4f7d16          *(uint64_t*)rax_17 = rsi;
0x4f7d21          rax_9 += 0x28;
0x4f7d34      }
0x4f7d34      
0x4f7e9b      int64_t i_1 = 0;
0x4f7e9d      int64_t rcx_15 = 0;
0x4f7e9f      int128_t* rdx_9 = nullptr;
0x4f7e9f      
0x4f7ee4      while (i_1 < 5)
0x4f7ee4      {
0x4f7f14          void* rax_22;
0x4f7f14          char rbx_13;
0x4f7f14          rax_22 = sub_40fd80(&data_50bde0, &var_148, i_1);
0x4f7f14          
0x4f7f1b          if (rbx_13 == 0)
0x4f7f1b          {
0x4f7f20              void* rax_23;
0x4f7f20              int64_t rbx_14;
0x4f7f20              rax_23 = sub_4f9660();
0x4f7f25              int128_t var_238 = zmm15;
0x4f7f2e              void* rax_24 = sub_409fe0(rax_23, rbx_14);
0x4f7f3a              var_238 = &data_505400;
0x4f7f42              *(uint64_t*)((char*)var_238)[8] = rax_24;
0x4f7f75              return access_denied(&data_543c58, data_5cd278, &var_238, 1);
0x4f7f1b          }
0x4f7f1b          
0x4f7ec0          int64_t rax_21;
0x4f7ec0          rax_21 = sub_447920(nullptr, rcx_15, rdx_9, *(uint64_t*)rax_22, *(uint64_t*)((char*)rax_22 + 8));
0x4f7ed0          rcx_15 = rax_21;
0x4f7ed3          i_1 += 1;
0x4f7ed6          rdx_9 = rbx_3;
0x4f7ee4      }
0x4f7ee4      
0x4f7f84      if (rdx_9 != 0x26)
0x4f7f84      {
0x4f8090          void* rax_29;
0x4f8090          int64_t rbx_18;
0x4f8090          rax_29 = sub_4f9aa0();
0x4f8095          int128_t var_38 = zmm15;
0x4f80a0          void* rax_30 = sub_409fe0(rax_29, rbx_18);
0x4f80ac          var_38 = &data_505400;
0x4f80b4          *(uint64_t*)((char*)var_38)[8] = rax_30;
0x4f80e7          return access_denied(&data_543c58, data_5cd278, &var_38, 1);
0x4f7f84      }
0x4f7f84      
0x4f7f8a      data_5cd538 = 0x26;
0x4f7f8a      
0x4f7f9c      if ((*(uint32_t*)data_62dd30) != 0)
0x4f7f9c      {
0x4f7fa0          int64_t* r11_2 = sub_459220(i_1, rbx_3, rcx_15, rdi_2, rsi, r8, r9, r10);
0x4f7fa5          *(uint64_t*)r11_2 = rcx_15;
0x4f7faf          r11_2[1] = data_5cd530;
0x4f7f9c      }
// ...
0x4f8002      access_denied(&data_543c58, data_5cd278, &var_18, 1);
0x4f8012      int64_t var_31b;
0x4f8012      __builtin_strncpy(&var_31b, "W#.s&`}I", 8);
0x4f8021      int64_t var_313;
0x4f8021      __builtin_memcpy(&var_313, "\x3f\x0b\x38\xde\x08\xbe\x6f\x2d\xd3\xc8\x3d\x31\xb9\x94\x15\xfd\x4e\x8a\x30\x53\x71\x1c\x94\x38\x45\x4e\x21\x92\x7f\xf6\xa2\x2c\x87\xe7\x5a\x6d\x10\x08\x49\x38\x0a\x79\x18\xdb\x05\x8a\x54\x30\x0c\xfb\x33", 0x33);
0x4f8021      
0x4f8106      for (int64_t i_2 = 0; i_2 < 0x3b; i_2 += 1)
0x4f80fa          *(uint8_t*)(&var_31b + i_2) += *(uint8_t*)(i_2 + &data_528adb);
0x4f80fa      
// ...
0x4f818b      aJN_mJlUHQ_Hi4Y5mpIpnyo(&data_543c58, data_5cd278, rax_33, rbx_21, &var_28, 1, 1);
0x4f819d      return sub_4f81c0();
0x4f7a00  }
```

We start our good old binja debugged and try `JNE`-ing the conditions that contain the `access_denied()` function. We eventually end up with a final:

```
Actually, I don't feel like printing the flag...
...but I can tell you that the flag is 38 characters long.
```

This pretty much means that we can probably read the flag somewhere in the memory. So I carefully step through the function by paying attention to the registers.

Bingo ! Around the loop at `0x4f81ae`, we can see chunks of data passing in the `r12` register. We setup breakpoints before and after each iteration, jump over previous exit conditions:

```c
BREAK 0x4f7db2  void* rax_15 = sub_444800(...);
      0x4f7db2  
      0x4f81ae  for (int64_t j = 0; j < var_258_1; j += 1)
      0x4f81a4      *(uint8_t*)((char*)rax_15 + j) = ((int8_t)!(((uint32_t)*(uint8_t*)((char*)rcx_8 + j))));
      0x4f81a4  
BREAK 0x4f7dd6  void* rax_16;
```

We see the following values passing in our registers:

```python
["32b2", "221fccaa8", "42024a30b", "edda76fdc2"]
```

Their lengths effectively add up to 32 (`38 - len("flag{}") = 32`), and as I was too lazy to understand in which order they actually went, I just computed all their permutations with

```python
import itertools
strings = ["32b2", "221fccaa8", "42024a30b", "edda76fdc2"]
print("\n".join([f"flag{{{''.join(p)}}}" for p in itertools.permutations(strings)]))
```

After a bit of trial and error, we eventually get `42024a30b 221fccaa8 edda76fdc2 32b2` as the correct combination. Flagged !