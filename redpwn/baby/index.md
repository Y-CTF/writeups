+++
title = "Baby"
date = 2021-07-27
authors = ["carcajou"]

[taxonomies]
categories = ["crypto"]
+++


# Baby

> n: 228430203128652625114739053365339856393 
>
> e: 65537 
>
> c: 126721104148692049427127809839057445790

Lien ctftime pour voir d'autres writeups : [https://ctftime.org/writeup/29247](https://ctftime.org/writeup/29247)

## Principe

On peut voir que n est très petit, ce qui sous-entendant qu'il est possible de le factoriser afin de retrouver p et q.

On peut le faire en utilisant SageMath : **factor(n)**

Une fois p et q obtenue, on peut alors calculer phi(n) 
$$
φ(n) = (p - 1)(q - 1)
$$
Puis on calcule la clé privée d en utilisant la fonction *inverse_mod* proposé par Sage



## Remarques

Pour convertir les long en byte, il faut importer la librairie python Crypto.Util.number 

```python
from Crypto.Util.number import long_to_bytes
d = inverse_mod(e, phi)
m = c ^ d
m = long_to_bytes(m)
print("Decrypted message : ", m.decode('utf-8'))
```



- D'autres équipes ont utilisées l'outil RsaCtfTool :

[https://github.com/Ganapati/RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)