#include <stdio.h>
int main(){
    int a = 3;
    int b = 7;
    switch (a%2)
    {
    case 3 : b = b + a;
    } // 1이나오는데 default도 없고 case 1도 없어 실행하지 않는다.
    printf("%d %d",a,b); //3 7 break가 없어 모두 연산
}