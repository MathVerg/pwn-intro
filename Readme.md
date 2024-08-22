# Introduction à l'exploitation de binaire

Slides et code d'un talk donné pour [Root-Me](https://www.root-me.org/) sur [Twitch](https://www.twitch.tv/rootme_org) le 2 août 2024. La rediffusion est disponible sur [YouTube](https://www.youtube.com/watch?v=TdQa6QwyovI).

Les binaires peuvent être compilés avec `make`. Les offsets ne seront pas forcément les mêmes que ceux que j'ai mis dans mes exploits, à vous de les adapter ^^

Liens des différents tools utilisés dans la présentation :
- [gef de bata24](https://github.com/bata24/gef)
- [pwntools](https://github.com/Gallopsled/pwntools/)
- [ROPgadget](https://github.com/JonathanSalwan/ROPgadget)
- [one_gagdget](https://github.com/david942j/one_gadget)
- [iaito](https://github.com/radareorg/iaito/)

Les différents flags utilisés dans le Makefile :
- `-fno-stack-protector`: désactive les canaries (qui sont là par défaut)
- `-zexecstack`: rend la stack exécutable
- `-no-pie`: désactive la PIE, je n'en ai pas trop parlé dans le talk, mais en gros, la PIE permet de randomiser l'adresse du binaire (en plus de celles de la libc, de la stack et du heap) via l'ASLR

Pour désactiver temporairement l'ASLR :
```
echo 0 > /proc/sys/kernel/randomize_va_space
```

Pour s'entraîner : https://www.root-me.org/fr/Challenges/App-Systeme/, tous les challs qui s'appellent ELF "x86/x64 - Stack buffer overflow".
