+++
title = "Plantopia"
description = "Plantopia is our brand-new, cutting-edge plant care management website! Designed for hobbyists and professionals alike, it's your one-stop shop for all plant care needs.  \n  \nPlease perform a penetration test before our site launch and let us know if you find any issues.  \n  \nUsername: `testuser`  \nPassword: `testpassword`  \n  \n**Press the `Start` button on the top-right to begin this challenge.**"
authors = ["Tyr"]
date = 2024-09-30

[taxonomies]
categories = []
+++

## Description

Plantopia is our brand-new, cutting-edge plant care management website! Designed for hobbyists and professionals alike, it's your one-stop shop for all plant care needs.  
  
Please perform a penetration test before our site launch and let us know if you find any issues.  
  
Username: `testuser`  
Password: `testpassword`  
  
**Press the `Start` button on the top-right to begin this challenge.**

----

As expected, we see a login page where we can use the provided credentials to access the website.
![](https://i.imgur.com/ebmAwzH.png)

While exploring, we find an API Docs page with Swagger that lists several web requests:
![](https://i.imgur.com/05AyLWj.png)

For authentication, we need a session cookie, so let's intercept the traffic using Burp Suite.
![](https://i.imgur.com/f1pk6dQ.png)

Here is the session cookie: `dGVzdHVzZXIuMC4xNzMwMzA0Mjgw`. Decoded from base64, it reveals `testuser.0.1730304280`:
- `testuser`: the username in use
- `0`: a role indicator or user type
- `1730304280`: a UNIX timestamp, likely the session expiration date or creation time

With this session cookie, the only available HTTP request in Swagger is `GET /api/plants`. Let's see if modifying it works.
![](https://i.imgur.com/Mzu8hWc.png)

Success! We're now logged in as `admin` by changing the values to `admin.1.1730304280` and encoding it as `YWRtaW4uMS4xNzMwMzA0Mjgw`. Using the [Cookie-Editor browser extension ](https://cookie-editor.com), we can make this session cookie persistent.
![](https://i.imgur.com/dtDuUvL.png)

In the `Admin` page, we can select a plant and modify various data related to it. One of the options sends an alert message with `/usr/sbin/sendmail -t`. Since this command is triggered via the API Docs, we add `&& ls -al` to it and trigger it.
![](https://i.imgur.com/oX0qQao.png)

To execute, we enter our admin session cookie and select the plant ID with the modified alert command (which is `1` in this case).
![](https://i.imgur.com/IjYLTEO.png)

It worked! Our command was executed successfully.
![](https://i.imgur.com/cQaSN4i.png)

But where can we view the output?.. If you noticed earlier, we now have access to the `Logs` page. Perfect!
![](https://i.imgur.com/xXtXqny.png)

Here, we see the command output, showing the `flag.txt` file in the current directory. Replacing `ls -al` with `cat flag.txt`, we trigger the command again and check the logs.
![](https://i.imgur.com/SFVchBw.png)

The flag is: `flag{c29c4d53fc432f7caeb573a9f6eae6c6}`
