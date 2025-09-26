+++
title = "Keybase"
authors = ["carcajou"]
date = 2021-08-28

[taxonomies]
categories = ["crypto"]
+++
Ce challenge portait sur une attaque avec un Accès à un oracle de chiffrement sur AES-CBC.

N'ayant pas réussi à résoudre ce challenge, vous trouverez en suivant le lien ci-dessous 2 writes-up avec la résolution complète : [https://ctftime.org/task/16740](https://ctftime.org/task/16740)

Ci-dessous, voici un récapitulatif de la solution

## Présentation

On pouvait envoyait un bloc de 32 bytes à chiffrer à l'oracle. Celui-ci renvoyait 

- une partie de la clé (14 bytes), 
- le 1er bloc de texte chiffré (16 bytes) 
- ainsi qu'une partie du 2ème bloc de texte chiffré (si ma mémoire est bonne)

Les 2 bytes manquant de la clé pouvait être brute-forcé car cela fait seulement 2^16 possibilités.

Pour l'IV c'était un peu plus compliqués vu qu'on avait 2^128 possibilités.

La faille résidait dans le fait qu'on pouvait envoyer avec pwntools un message de 32 bytes à 0 (32 * '\0'). Ainsi avant le chiffrement, on avait IV XOR '\'\0' ce qui avait pour conséquent que seulement l'IV était chiffré.

### Attaque

- Pour toutes les possibilités de clés :
  - Déchiffrer l'IV chiffré (Ciphertext bloc 1) avec la clé essayé -> on obtient un IV
  - Il faut stocker la paire IV, Clé. En python une liste contenant des tuples représentant à chaque fois une paire clé - IV.
- Pour tous les IV obtenus, déchiffrer le message chiffré du challenge. Si on obtient un mot contenant le terme "flag" dedans => on a alors la bonne combinaison de clé/IV

## Schéma

Schéma simplifié du déchiffrement avec un message composé de 32 bytes nulls..

- En orange foncé, ce qu'on connait
- En clair, ce qu'on connait partiellement

![cbc-aes-Page-3](cbc-aes-Page-3.png)