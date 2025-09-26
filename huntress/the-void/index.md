+++
title = "The Void"
description = "When you gaze long into the void, the void gazes also into you..."
authors = ["ary.eth" ,"mango"]
date = 2024-09-30

[taxonomies]
categories = ["warmups"]
+++

## Description

When you gaze long into the void, the void gazes also into you...

----
### Solution

The server returns us what seems to be whitespaces;
![](https://i.imgur.com/VpFaFMq.png)

However, if you select enough of thoses "whitespaces" and copypaste them into anything that isnt your terminal (think notePad, Firefox...), you'll notice that you got the flag. This is because it is hidden with an [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)


(s.o. Mango for the explainations)