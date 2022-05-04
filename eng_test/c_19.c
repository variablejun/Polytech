#include <stdio.h>
struct KEY
{
    int a;
    int b;
};

int main(){
    struct KEY y;
    struct KEY *p;
    p = &y;
    y.a = 100;
    y.b = 200;
    printf("%d",p->a); //p가 가리키는 곳은 y의 주소이고 그안에 a에는 100이 들어있다.
}//100