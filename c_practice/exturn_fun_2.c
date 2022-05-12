#include <stdio.h>

extern int a;

void out_fun(void) {
    a = 10;
    printf("외부 out_fun 함수");
}