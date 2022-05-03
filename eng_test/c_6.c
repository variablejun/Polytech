#include <stdio.h>
void main(){
    int i = 0, sum = 0;
    while (i<10)
    {
        i++;
        if (i % 2 ==1) // 2로 나눈 나머지가 1 즉 홀수일때
        {
            continue; // 컨티뉴 분기문을 걸어주어 아래 명령문을 실행하지 않고 
            // 다시 while 문으로 올라간다.
        }
        sum = sum + i;
    }
    printf("%d ", sum); //30 
    
}