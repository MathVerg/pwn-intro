#include <stdio.h>
#include <unistd.h>

void win() {
    puts("Beep beep I'm a sheep");
}

void foo(unsigned int size) {
    char buf[16];
    read(fileno(stdin), buf, size);
    puts(buf);
    if (buf[0] == '2') {
        read(fileno(stdin), buf, size);
        puts(buf);
    }
}

int main() {
    puts("Hello world!");
    foo(100);
}