#include <stdio.h>
void main(){
    int a[3][5];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            a[i][j] = j * 3 +(i +1);
            printf("%d " ,a[i][j]);
        }
        printf("\n");
    }
    
}
/*
1 4 7 10 13 
2 5 8 11 14 
3 6 9 12 15 */