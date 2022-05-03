#include <stdio.h>
void main(){
    int i = 3;
    int k = 1;
    switch (i)
    {
    case 0:
    case 1:
    case 2:
    case 3: k = 0;
    case 4: k = k + 3;
    case 5: k = k - 10;

    default:
        k--;
        break;
    }
    printf("%d",k); // -8 
   // 스위치문은 break 만날때 까지 아래 명령문을 실행한다, 
   // 그래서 default 까지 실행하여 -8이 나오는것
}