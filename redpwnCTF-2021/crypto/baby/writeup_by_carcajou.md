## Baby

> n: 228430203128652625114739053365339856393 
>
> e: 65537 
>
> c: 126721104148692049427127809839057445790

Lien ctftime pour voir d'autres writeups : [https://ctftime.org/writeup/29247](https://ctftime.org/writeup/29247)

On peut voir que n est très petit, ce qui sous-entendant qu'il est possible de le factoriser afin de retrouver p et q.

On peut le faire en utilisant SageMath : factor(n)

Une fois p et q obtenue, on peut alors calculer phi(n) 
$$
φ(n) = (p - 1)(q - 1)
$$
Puis on calcule la clé privée d en utilisant la fonction *inverse_mod* proposé par Sage



D'autres équipes ont utilisées l'outil RsaCtfTool :

https://github.com/Ganapati/RsaCtfTool