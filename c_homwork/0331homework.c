#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>


int main(void) {
    printf("2개의 숫자를 입력하세요 : ");
    int num1, num2;
    scanf_s("%d %d", &num1, &num2);
    printf("두 수가 같은가? : %s\n", num1 == num2 ? "TRUE" : "FALSE");
    printf("num1이 더 큰가? : %s\n", num1 >= num2 ? "TRUE" : "FALSE");
    printf("num2는 양수인가? : %s\n", num2 >= 1 ? "TRUE" : "FALSE");
}