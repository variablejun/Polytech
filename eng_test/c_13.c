#include <stdio.h>
int Soojebi(int base, int exp){
    int i, result =1;
    for ( i = 0; i < exp; i++) // ~승까지 반복
    {
        result = result * base; // 계속 base를 곱하며 반복
    }
    return result;  
}

int main(){
    printf("%d", Soojebi(2,10));
}
//1024 base와 승을 지정해서 구하는 코드 2의 10승을 출력한다