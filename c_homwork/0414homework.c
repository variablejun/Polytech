/*1.제시된 실행 결과와 같이 숫자를 여러 개 입력하고 입력한 수의
 2배만큼 별표가 출력되도록 코드를 작성하세요. 단 반복문은 while 문을 사용하세요.

예를 들어 2314인경우 각 줄에 4개, 6개, 2개, 8개를 출력한다.
[실행결과]
숫자를 여러개를 입력하세요:2314
****
******
**
********
*/
#include <stdio.h>
int main(void){
    int star;

    printf("숫자를 여러개를 입력하세요 : ");
    scanf("%d",&star);
    int i;
    int j;
    int temp;
    int a = 1;
    while (1)
    {
        j = star % 10;
        if (j==0)
        {
            break;
        }

        while (j>=a)
        {
            printf("*");
            a++;
        }
        a = 1;
        printf("\n");
        star = star / 10;
        
        
    }
    
   
    
}
