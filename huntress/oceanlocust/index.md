+++
title = "OceanLocust"
description = "Wow-ee zow-ee!! Some advanced persistent threats have been doing some tricks with hiding payloads in image files!\n\nWe thought we would try our hand at it too.\n\nNOTE: this challenge includes a debug build of the binary used to craft the image, as well as a release build... so you may choose to go an easier route or a harder route ;)"
authors = ["mango"]
date = 2024-09-30

[taxonomies]
categories = ["reverse"]
+++

## Description

Wow-ee zow-ee!! Some advanced persistent threats have been doing some tricks with hiding payloads in image files!

We thought we would try our hand at it too.

NOTE: this challenge includes a debug build of the binary used to craft the image, as well as a release build... so you may choose to go an easier route or a harder route ;)

----

We are handed a 7-zip archive that contains 2 executables and one `png` image:

```
$ ll ocean_locust/Chal/
.rw-r--r--@ 6.9k acm  4 oct 09:48 inconspicuous.png
.rw-r--r--@ 477k acm  1 oct 12:25 png-challenge-debug.exe
.rw-r--r--@ 187k acm  1 oct 12:19 png-challenge.exe
```

Dynamic analysis reveals that some extra content passed to the program through command-line argument is added to the header and the footer of the PNG file that is fed to the program. We ran the program with the `20 * A`, `20 * B` and `10 * A + 10 * B` payloads to get some data. For instance, 20 B's gives us:

```=
02 62 69 54 62 20 2b 56 d8 40 97 
02 62 69 54 63 20 2b 57 1a 2a a0 
02 62 69 54 65 20 2b 53 97 56 12 
02 62 69 54 69 20 2b 5a 8d af 76 
02 62 69 54 64 20 2b 52 55 3c 25
02 62 69 54 66 20 2b 51 d1 e8 4b 
02 62 69 54 61 20 2b 54 9e fe ce 
02 62 69 54 68 20 2b 5b 4f c5 41 
02 62 69 54 6a 20 2b 58 cb 11 2f 
02 62 69 54 67 20 2b 50 13 82 7c 
```

Running the program with different images and identical payloads gives us near-identical results. Running the program multiple times on the same data also gives the same output. We hence guess that there is a clearly defined, 1-to-1 encoding that takes places within the binary. Another neat detail is that the number of lines times the first byte of the line (here `02`) gives us the length of the string.

Through sheer sweat observation, we finally get the hinsight that data is always encoded in the file using a similar pattern that uses the same `62 69 54` bytes (`biT` in ascii) near the start of each "sentence". We use this information to carve out the enciphered flag from the `inconspicuous.png` file.

- Header chunk:
    ```=
    05 62 69 54 68 06 59 29 C2 C8 0A AF 71 26 
    05 62 69 54 61 04 05 35 06 19 9D C5 69 88 
    05 62 69 54 62 04 0C 37 5A 55 0C B9 9F 21 
    05 62 69 54 64 5A 0C 37 5C 06 F9 FB AA 5E
    05 62 69 54 65 54 5C 36 5D 00 B7 20 36 7B 
    05 62 69 54 63 01 5F 6D 53 00 7D 55 D6 EC 
    05 62 69 54 66 00 58 64 03 07 A6 21 A5 2E
    ```

- Footer chunk:
    ```=
    05 62 69 54 67 55 0B 36 51 57 C8 E8 02 80
    05 62 69 54 68 06 59 29 C2 C8 0A AF 71 26
    05 62 69 54 61 04 05 35 06 19 9D C5 69 88 
    05 62 69 54 62 04 0C 37 5A 55 0C B9 9F 21 
    05 62 69 54 65 54 5C 36 5D 00 B7 20 36 7B 
    05 62 69 54 63 01 5F 6D 53 00 7D 55 D6 EC 
    05 62 69 54 66 00 58 64 03 07 A6 21 A5 2E 
    05 62 69 54 67 55 0B 36 51 57 C8 E8 02 80 
    ```

We've also discovered that the program sometimes pads the header and footer with repeated words from the flag. The 5th column of numbers is also quite... inconspicuous as it presents a neat pattern of incrementing integers. Once filtered and reordered, we get the following:

```=
05 62 69 54     61     04 05 35 06 19     9D C5 69 88 
05 62 69 54     62     04 0C 37 5A 55     0C B9 9F 21 
05 62 69 54     63     01 5F 6D 53 00     7D 55 D6 EC
05 62 69 54     64     5A 0C 37 5C 06     F9 FB AA 5E
05 62 69 54     65     54 5C 36 5D 00     B7 20 36 7B 
05 62 69 54     66     00 58 64 03 07     A6 21 A5 2E 
05 62 69 54     67     55 0B 36 51 57     C8 E8 02 80 
05 62 69 54     68     06 59 29 C2 C8     0A AF 71 26
```

And would you know it, `8 * 5 = 40` which is exactly the expected flag length. We now know that we're on the right track.

More analysis leads to the conclusion that the data is encoded in the following format:

`Chunk size | b | i | T | Index | Chunk1 | Chunk2 | Chunk3 | Chunk 4 | Chunk 5 | Padding / Trash`

The next step is to encode a factice flag and see what the `flag{` characters encode to. If we try to encore `flag{AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA}`, we indeed get `05 62 69 54 67 55 0B 36 51 57 C8 E8 02 80` as our first line.

The logical next step is to create a dictionnary in order to decode the flag. We feed the following strings as input to the program and carve out the data:

- `flag{abcdefghijklmnopqrstuvwxyzABCDEFGH}`
- `flag{ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567}`
- `flag{89.-/_............................}`

As expected, we observe that the first line never changes. We are nonetheless hitting a wall because there are multiple caracters that encode to the same number. The algorithm hence must not use a simple 1-to-1 conversion mechanism. 

Through more observation and some static analysis, we found that the first 3 gylphs of the payload are simply xored' with the `biT` string. Strong with this discovery, and helped by the fast that xor is an easily reversible operation, we get to work on the first line using our crib (`flag{`) and our ciphertext `05 62 69 54 61 04 05 35 06 19 9D C5 69 88`.

We know that:

- `04 05 35` is "fla"
- `06` must be "g"
- `19` must be "{"

What is don't know is how the letters "g" and "{" were encoded. If we tinker and take the ascii values for these letters and xor them with the data in the ciphertext, we get:

- `g ^ 0x06 = 0x67 ^ 0x06 = 0x61`
- `{ ^ 0x19 = 0x7B ^ 0x19 = 0x62` 

Which happen to be the 5th and 2nd bytes in our line, respectively. We've discovered that for each line, the key is contained within the line itself. For the first line:

- `62 69 54 61 62` is the XOR key
- `04 05 35 06 19` is the ciphertext

XOR'ing both together indeed gives `f l a g {`.

We now only need to piece together a script to decode the whole ciphertext. The relevant part is the following:

```python
def xor_decrypt(cipher):
    result = []
    i = 0x61

    for group in cipher:
        key = [0x62, 0x69, 0x54, i, 0x62]
        xored_bytes = [group[j] ^ key[j] for j in range(5)]

        result.append("".join(chr(b) for b in xored_bytes))
        i += 1

    return "".join(result)
```

Running the script on the data that was carved out of the PNG file indeed gives us the flag: `flag{fec87c690b8ec8d65b8bb10ee7bb65d0}`.