
char data[] = "Hello";

long func(long a, long b) {
    data[0] = 'h';
    return (a ^ 42l) - b;
}

int _start() {
    return 0;
}
