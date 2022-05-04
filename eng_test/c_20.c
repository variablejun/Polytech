#include <stdio.h>


int main(){
    int a = 2, b = 5, c = 3;
    b /= a; // 5 를 2 로 나누면 2.5 이지만 정수형이기 때문에 2가 대입 
    c %= a; // 3을 2로 나누어 나머지를 대입하면 1
    printf("%d %d", b, c);
}//2 1