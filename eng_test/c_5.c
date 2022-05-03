#include <stdio.h>
int r1(){
    return 4;
}

int r10(){
    return (30 + r1());
}

int r100(){
    return (200+r10());
}

int main(){
    printf("%d \n", r100()); //234 선언된 재귀함수를 모두 호출하여 연산된 것이다.
    return 0;
}