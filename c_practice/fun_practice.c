#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void){
    int start, end;
    int temp;
    printf("시작값: ");
    scanf("%d",&start);
    printf(" 끝값: ");
    scanf("%d", &end);
    if (end >= start)
    {
        temp = start;
        start = end;
        end = temp;
    }
    for ( int i = end; start >= i; i++){
        
        if(i % 2 == 1)
        {
            printf("%d",i);
        }
    }
}