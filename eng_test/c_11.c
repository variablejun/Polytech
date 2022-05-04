#include <stdio.h>
int main(){
   int i, j = 0;
   for (i = 0; i <= 5; i++)
   {
       j = j + i; // i의 누적합계를 가진다
       printf("%d",i);
       if (i == 5) // i가 5까지 반복하면서 누적된 합계를 출력
       {
           printf(" = ");
           printf("%d",j);
       }else{
           printf(" + ");
       }
       
   }
   
}
// 0 + 1 + 2 + 3 + 4 + 5 = 15