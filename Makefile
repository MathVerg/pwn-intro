.PHONY := all clean

TARGETS := execstack canary rop asm

CFLAGS := -Wall -Wextra

all: $(TARGETS)

execstack: vuln.c
	gcc $(CFLAGS) -fno-stack-protector -o execstack vuln.c -zexecstack -no-pie

canary: vuln.c
	gcc $(CFLAGS) -o canary vuln.c -zexecstack -no-pie

rop: vuln.c
	gcc $(CFLAGS) -fno-stack-protector -o rop vuln.c

asm.s: asm.c
	gcc $(CFLAGS) -S -O1 -masm=intel -o asm.s asm.c

asm: asm.s
	gcc $(CFLAGS) -o asm asm.s -nostdlib

clean:
	rm $(TARGETS) *.s