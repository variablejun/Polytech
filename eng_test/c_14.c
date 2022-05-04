#include <stdio.h>
int main(){
    int a = 3, b = 4, c = 3, d = 5;
    if ((a == 2 || a == c) & !(c > d) & (1 == b ^ c != d))
    {
        a = b + c;
        if (7 == b ^ c != a)
        {
           printf("%d",a);
        }else{
           printf("%d",b);
        }

    }else{
        a = c + d;
        if (7 == c ^ d != a)
        {
            printf("%d", a);
        }else{
            printf("%d", d);
        }
        
    }
    
}
//7