#include <stdio.h>
void main(){
    int i, j;
    int temp;
    int a[5] = {75,95,85,100,50};
    for ( i = 0; i < 4; i++)
    {
        for ( j = 0; j < 4-i; j++) 
        {
            if (a[j] > a[j + 1]) // 앞에 두가지를 비교해 자리를 바꾸는 버블정렬이다
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
            
        }
        
    }
    for ( i = 0; i < 5; i++)
    {
        printf("%d ", a[i]); // 50 75 85 95 100
    }
    
    
}