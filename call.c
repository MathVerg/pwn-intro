int truc(int x) {
    int y = 8;
    return x + y;
}

int bar() {
    int x = 3;
    int y = 5;
    y = truc(x);
    return y;
}

void foo() {
    truc(2);
    bar();
}

int main() {
    int result = bar();
    return result;
}