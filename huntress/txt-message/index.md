+++
title = "TXT Message"
description = "Hmmm, have you seen some of the strange DNS records for the ctf.games domain? One of them sure is odd... "
authors = ["Unknown"]
date = 2024-09-30

[taxonomies]
categories = ["warmups"]
+++

## Description

Hmmm, have you seen some of the strange DNS records for the ctf.games domain? One of them sure is odd... 

----

```bash
dig -t txt ctf.games

; <<>> DiG 9.18.28 <<>> -t txt ctf.games
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47416
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;ctf.games.			IN	TXT

;; ANSWER SECTION:
ctf.games.		14400	IN	TXT	"146 154 141 147 173 061 064 145 060 067 062 146 067 060 065 144 064 065 070 070 062 064 060 061 144 061 064 061 143 065 066 062 146 144 143 060 142 175"

;; Query time: 26 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Sun Oct 06 21:28:00 CEST 2024
;; MSG SIZE  rcvd: 202
```

We'll then decode from octal to ascii

```bash
echo "146 154 141 147 173 061 064 145 060 067 062 146 067 060 065 144 064 065 070 070 062 064 060 061 144 061 064 061 143 065 066 062 146 144 143 060 142 175" \
| awk '{for(i=1;i<=NF;i++) printf("%c", strtonum("0"$i))} END {print ""}'
```

Which indeed gives us the flag `flag{14e072f705d45882401d141c562fdc0b}`.