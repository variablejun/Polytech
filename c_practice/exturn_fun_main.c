#include <stdio.h>

int a;
static int b;

void in_fun(void);
extern void out_fun(void);

int main(void) {
    printf("전역 변수로 외부 연결 함수 호출\n");
    printf("키워드 사용 extern \n");

    out_fun();
    printf("1. 외부 연결값 출력 %d \n", a);
    printf("정적 지역 변수 내부 연결 함수 호출");
    printf("키워드 사용 static \n");

    in_fun();
    printf("2. 외부 연결 함수에서 값 출력 %d \n", b);

}

void in_fun(void) {
    b = 20;
    printf("\n [내부 in_fun() 함수 영역] \n");
}