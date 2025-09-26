+++
title = "PillowFight"
description = "PillowFight uses _**advanced AI/MLRegressionLearning**_ to combine two images of your choosing  \n  \n*note to investors this is not techically true at the moment we're using a python library but please give us money and we'll deliver it we promise.  \n  \n**Press the `Start` button on the top-right to begin this challenge.**"
authors = ["Tyr"]
date = 2024-09-30

[taxonomies]
categories = []
+++

## Description

PillowFight uses _**advanced AI/MLRegressionLearning**_ to combine two images of your choosing  
  
*note to investors this is not techically true at the moment we're using a python library but please give us money and we'll deliver it we promise.  
  
**Press the `Start` button on the top-right to begin this challenge.**

----

Upon accessing the website, we find a form that allows uploading two images and combining them. There’s also a hint about API documentation available at `/swagger`. Exploring this documentation reveals an endpoint, `/combine`, where we can specify images along with an `eval_command` parameter for custom operations. Let’s test it by attempting to combine two images:
![](https://i.imgur.com/DhWShYz.png)

Here's what we've got:
![](https://i.imgur.com/5PwNDCv.png)

Let’s try using a different custom `eval_command` instead of `convert()` in the previous formData, maybe can we do some command injection.
![](https://i.imgur.com/ZgrT7eX.png)

This attempt results in a "Bad Request", with the following response:
```json
{
  "error": "'str' object has no attribute 'save'"
}
```

It appears that the server expects an image output with a `.save()` attribute. So, what if we raise an exception instead to see the error response? Let's try this:
```Python
exec('raise Exception(open("flag.txt").read())')
```

Bingo! The flag appears in the response body as part of the error message.
![](https://i.imgur.com/ap64jNt.png)

The flag is: `flag{b6b62e6c5cdfda3b3a8b87d90fd48d01}`
