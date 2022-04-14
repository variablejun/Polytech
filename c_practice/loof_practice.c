#include <stdio.h>
int main(void){
    int star = 10;

    for (int i = 0; i < star; i++)
    {
        if (i >5)
        {
        for (int j = 0; j < (star - i); j++)
        {
            printf("*");
        }
        printf("\n");
        }
        else{
        for (int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
        }
    }
    
}