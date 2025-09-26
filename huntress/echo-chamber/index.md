+++
title = "Echo Chamber"
description = "Is anyone there? Is anyone there? I'm sending myself the flag! I'm sending myself the flag! "
authors = ["glys"]
date = 2024-09-30

[taxonomies]
categories = ["forensics", "scripting"]
+++

## Description

Is anyone there? Is anyone there? I'm sending myself the flag! I'm sending myself the flag! 

----

We are given a pcap with what seems to be only icmp (ping) packets.

Opening it in wireshark we inspect packet fields and find a data field containing what looks like repeating hex byte data.

![](https://i.imgur.com/Pz0jPgm.png)

So we extract it to a file, making sure we only take one side of the communications (`icmp.type == 8`) since seems like all requests are echoed with same data
```bash
   huntress tshark -2 -r echo_chamber.pcap -R "data.data && icmp.type == 8" -T fields -e data.data > content
   huntress head content
89898989898989898989898989898989898989898989898989898989898989898989898989898989
50505050505050505050505050505050505050505050505050505050505050505050505050505050
4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e4e
47474747474747474747474747474747474747474747474747474747474747474747474747474747
0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d
0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a
1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a
0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
```

These really look like a sequence of hex encoded bytes.
Let's take first 2 chars each line and decode

```bash
   huntress cut -c 1-2 content | tr -d '\n' | xxd -r -p > out
   huntress file out
out: PNG image data, 1961 x 139, 8-bit grayscale, non-interlaced
   huntress exiftool out
...
Caption                         : flag{6b38aa917a754d8bf384dc73fde633ad}
...
```

The image also is the flag

![](https://i.imgur.com/NYG4zcg.png)

