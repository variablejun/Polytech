#include <stdio.h>
int main(){
    int a = 5;
    int s = 0;
    switch (a/2)
    {
    case 2 : s++;
    case 3 : a = a + s;
    
    default:
        a++;
    }
    printf("%d %d",s,a); //1 , 7 break가 없어 모두 연산
}