#include <stdio.h>
void main(){
    int i = 0, c = 0;
    while (i < 10)
    {
        i++;
        c = c * i; // c는 0이다 뭘 곱해도 0이다.
    }
    printf("%d", c); //0 그래서 0이나온다.
    
}