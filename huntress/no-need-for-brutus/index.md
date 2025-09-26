+++
title = "No need for Brutus"
description = "Author: @aenygma\n\nA simple message for you to decipher:\n\nsquiqhyiiycfbudeduutvehrhkjki\n\nSubmit the original plaintext hashed with MD5, wrapped between the usual flag format: flag{}\n\nEx: If the deciphered text is \"hello world\", the MD5 hash would be 5eb63bbbe01eeed093cb22bb8f5acdc3, and the flag would be flag{5eb63bbbe01eeed093cb22bb8f5acdc3}."
authors = ["Ary.eth"]
date = 2024-09-30

[taxonomies]
categories = ["crypto"]
+++

## Description

Author: @aenygma

A simple message for you to decipher:

squiqhyiiycfbudeduutvehrhkjki

Submit the original plaintext hashed with MD5, wrapped between the usual flag format: flag{}

Ex: If the deciphered text is "hello world", the MD5 hash would be 5eb63bbbe01eeed093cb22bb8f5acdc3, and the flag would be flag{5eb63bbbe01eeed093cb22bb8f5acdc3}.

----
## Solution

Brutus killing Caesar once again.

We open up [DCode on the ceasar cipher decryption](https://www.dcode.fr/caesar-cipher), and input our simple message.

Press decrypt and bingo, `caesarissimplenoneedforbrutus`

Just one little step before flagging, we encrypt it in MD5, still on [DCode](https://www.dcode.fr/md5-hash), giving us `c945bb2173e7da5a292527bbbc825d3f`.

After adding the flag format, we can flag this challenge.

