+++
title = "Farm"
authors = ["leonard-besseau"]
date = 2021-08-01

[taxonomies]
categories = ["crypto"]
+++

# Crypto CTF 2021 Writeup Challenge Farm

For this task, we are given two file: the code and the encrypted flag.

```python
#!/usr/bin/env sage

from sage.all import *
import string, base64, math
from flag import flag

ALPHABET = string.printable[:62] + '\\='

F = list(GF(64))

def keygen(l):
	key = [F[randint(1, 63)] for _ in range(l)] 
	key = math.prod(key) # Optimization the key length :D
	return key

def maptofarm(c):
	assert c in ALPHABET
	return F[ALPHABET.index(c)]

def encrypt(msg, key):
	m64 = base64.b64encode(msg)
	enc, pkey = '', key**5 + key**3 + key**2 + 1
	for m in m64:
		enc += ALPHABET[F.index(pkey * maptofarm(chr(m)))]
	return enc

# KEEP IT SECRET 
key = keygen(14) # I think 64**14 > 2**64 is not brute-forcible :P

enc = encrypt(flag, key)
print(f'enc = {enc}')
```

```enc = 805c9GMYuD5RefTmabUNfS9N9YrkwbAbdZE0df91uCEytcoy9FDSbZ8Ay8jj```

We can see that the alphabet is mapped to polynomial in GF(64). The encryption is a simple linear substitution of each character of the flag in base64 and can be easily reversed.

```
Encrypted Char = key * Char
```

Which can be reversed to 

```
Char = (Encrypted Char) / key
```

We just need to find the key and for this we can use the fact the flag must begin by `CCTF{` (`Q0NURns=` in base 64) to find it because

```
key = (Encrypted Char) / Char
```

## Implementation

```python
import string, base64, math

ALPHABET = string.printable[:62] + '\\='

F = list(GF(64))

enc = '805c9GMYuD5RefTmabUNfS9N9YrkwbAbdZE0df91uCEytcoy9FDSbZ8Ay8jj'

def maptofarm(c):
	assert c in ALPHABET
	return F[ALPHABET.index(c)]

inv_F = {} 
index = 0                                                               
for i in F: 
    inv_F[i] = index 
    index+=1

inv_dict = {}
index = 0
for i in ALPHABET: 
     inv_dict[i] = index 
     index+=1

key_target = F[8]/maptofarm('Q') # Key used to compute value


res = ''                                                                  
for i in enc: 
    res += ALPHABET[inv_F[F[inv_dict[i]]/key_target]]

print(base64.b64decode(res))
```

and the flag is `CCTF{EnCrYp7I0n_4nD_5u8STitUtIn9_iN_Fi3Ld!}`

