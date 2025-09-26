+++
title = "Wolf"
date = 2021-08-03
authors = ["leonard-besseau"]

[taxonomies]
categories = ["crypto"]
+++

**Not solved during the CTF** :(

For this task we are given the source code and an encryption oracle.

So we can see that the encryption use GCM and that the password is hard-coded. The message are encrypted with the following structure (HEADER|MESSAGE|PADDING) 

![](https://upload.wikimedia.org/wikipedia/commons/2/25/GCM-Galois_Counter_Mode_with_IV.svg)

My first idea was to recover the nonce as the header is predictable in order to decrypt the message normally. 

```
nonce = ECB_decrypt(plaintext XOR CipherText) - 2
```

this was not possible as it appears that the library generates a new nonce for the CTR if the nonce is smaller than 12 bytes.

## Solution

As the program reuse the nonce it leaks the XOR of the plaintexts so we just have to ask for one encrypted text, XOR it with the encrypted flag and XOR the result with the known plain text.

```python
a = xor(bytes.fromhex('7c02c166645f83517e842bafef2572736ec1922599cceebaf218d991ad5853c40b81e0f3c70ef39bb22cb113ea9ae4ec05aae0dd495e6181cd98740ef1a1c1c70dd9888ca46aaaeeccc898c75268f8cfec09c8fa0060ff0c5c1e7125c279c24d'),
             bytes.fromhex('7c02c166645f83517e842bafef2572746ee0b313bdd5d387cf25ccc3a34c54f536bcddcec658ffa68f118c13eda7d9d138ace3d1125971d3daa94933cc9cd79530e4b5b1b63ba7fcc2efa5fa6f55bb8caf4a8bb91f3fa05303412e7a9d269d129c5ca2904a34cb19c2d8172f163598ded98481a43db9d7701d4e148c1a803efc'))

    b = xor(b'\x00'*16+b'\nbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'+b'='+b'\x00', a)
    print(b)
```

and the flag is 

```
CCTF{____w0lveS____c4n____be____dan9er0uS____t0____p3oplE____!!!!!!}
```



