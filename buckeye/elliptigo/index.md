+++
title = "Elliptigo"
date = 2021-10-27
authors = ["leonard-besseau"]

[taxonomies]
categories = ["crypto"]
+++

## BuckeyeCTF

We are given an implementation of the 25519 curve and are allowed to give a base point use to generate a private key for AES. Since we can choose the base point (The generator we should try to generate an anomalous curve).

By looking [here](https://cr.yp.to/ecdh.html#validate), we can see there already is some point that have a low order. We can take any and then we can decrypt the message with either (0, 1 the point or the other 5 possibilities).

This gives us the flag `buckeye{p01nt5_0f_l0w_0rd3r}`

