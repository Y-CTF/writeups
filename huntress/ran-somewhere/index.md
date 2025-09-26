+++
title = "Ran Somewhere"
description = "Thanks for joining the help desk! Here's your first ticket of the day; can you help the client out?\n\nNOTE, this challenge uses a non-standard flag format. Enter the human-readable name of the location. "
authors = ["Ary.eth"]
date = 2024-09-30

[taxonomies]
categories = ["osint"]
+++

## Description

Author: @Spyderwall

Thanks for joining the help desk! Here's your first ticket of the day; can you help the client out?

NOTE, this challenge uses a non-standard flag format. Enter !
the human-readable name of the location. 

----

## Resolution

We recieve  an .eml file, containing a mail with the following :

Help Me IT!! My USB was stolen! I was headed into town for some work and stopped by a client's coffee shop to get work done. Everything was fine; I was working and drinking coffee. I got up to use the restroom; when I returned, I saw that my computer had been tampered with! All my work was closed out, and my flash drive with my projects was gone! I can't lose this; there was very important work on it! I thought the security tools you put in place would stop something like this!!
When I was looking at the desktop, I noticed three new files that were not there before. I opened one to see if they were my files, but they are a jumbled mess. I can't make any sense of it. I think it is that "ran somewhere" that your team keeps warning us about. I still don't know what it is, but please reverse this and get my USB back. I can't believe this happened!
I am attaching those files so you can fix them. 

-Mack Eroni
 President
 
 [Check out our new website!](https://sites.google.com/view/id-10-t/home)
 
 ---
 
 attached are two files with no extension, and a .txt.
 
 By checking out the mail, we can see a website called id10t solutions.
 Under their feedback section, we can see `Z Vault Coffee Shop`, and `Not Licensed to provide solutions to anyone or anywhere, especially Maryland`
 
 We can find pretty quickly where the `Z Vault Coffee Shop` is by googling it, and confirming the 2nd hint; it's located in `Bel Air, Maryland US`.
 
 ### Alright, but what about thoses mysterious files ?
 
 By opening them with a file editor, we can see the `JFIF` tag on the first line.
 
 By appending the extension `.jfif`, we can then open thoses two files which seem to be images.
 
 ![](https://i.imgur.com/IhCzSiG.jpeg)
![](https://i.imgur.com/pAAuzcb.jpeg)

 
 ### And for the .txt ?
 
 opening the .txt with a file editor reveals some hex. Quick [CyberChef](https://gchq.github.io/CyberChef/) hex to ASCII, and the following message uncovers :
`Hey There! You should be more careful next time and not leave your computer unlocked and unattended! You never know what might happen. Well in this case, you lost your flash drive. Don't worry, I will keep it safe and sound. Actually you could say it is now 'fortified'. You can come retrieve it, but you got to find it. I left a couple of files that should help.- Vigil Ante`

### What now ?

With all the info we have, we know we are looking for the location where the pictures were taken; location which should be in Bel Air, Maryland, maybe near the `Z Vault Coffee Shop` ?

We can observe some castle-like structure in the image, and a distinct red road pattern with a chessboard tileset.

Googling `Bel Air Maryland castle` shows us as a first suggestion [The Bel Air Armory](https://www.belairmd.org/499/History) website.

Let's go to Google Maps to see what that armory looks like...

Aaaand [Bingo.](https://www.google.com/maps/place/Bel+Air+Armory/@39.5375298,-76.3500837,3a,90y,295.93h,101.88t/data=!3m8!1e1!3m6!1sAF1QipPbSf9G5gVPWDnDUqKKIV1s0oSYkBe36fSXK1Zy!2e10!3e11!6s%2F%2Flh5.ggpht.com%2Fp%2FAF1QipPbSf9G5gVPWDnDUqKKIV1s0oSYkBe36fSXK1Zy%3Dw900-h600-k-no-pi-11.880944447891821-ya295.933260342317-ro0-fo100!7i5376!8i2688!4m11!1m2!2m1!1sbel+air+maryland+castle!3m7!1s0x89c7ddcdc37c7e81:0x47840dfee3716b01!8m2!3d39.5375218!4d-76.3503229!10e5!15sChdiZWwgYWlyIG1hcnlsYW5kIGNhc3RsZVoZIhdiZWwgYWlyIG1hcnlsYW5kIGNhc3RsZZIBEGNvbW11bml0eV9jZW50ZXKaASRDaGREU1VoTk1HOW5TMFZKUTBGblNVUXliR1pRU0RCUlJSQULgAQA!16s%2Fm%2F05bzvmq?coh=205410&entry=ttu&g_ep=EgoyMDI0MTAwNy4xIKXMDSoASAFQAw%3D%3D)


