#include <stdio.h>
void main(){
    char *p = "KOREA"; // 0 1 2 3 4
    printf("%s\n", p); //KOREA 전체 문자열 출력
    printf("%s\n", p +3); //EA 배열 3번째 방(4) 부터 출력
    printf("%c\n", *p); // K p 배열 메모리 0번째 방 출력
    printf("%c\n", *(p+3)); // E 배열 메모리 4번째 방 출력 p = 4
    printf("%c\n", *p + 2); // *p 가 가리키는 K에다가 2를 더하면 아스키 코드 값이 더해저 M이 나온다

}