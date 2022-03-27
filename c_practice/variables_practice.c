#include <stdio.h>
int main(void){
    int num = 5; // 변수 선언과 동시에 초기화
    int num2 = 3;
    printf("%d \n",num);
    printf("%lu \n",sizeof(num));  // unsigned long
    /*자료형의 크기는 0이 될 수 없어 unsigned 이다.
    sizeof의 반환형은 단순한 int형가 아닌 long unsigned int형
    https://sckllo7.tistory.com/entry/sizeof-연산의-함정
    */
    float result;
    //result = num/num2;  1.00000
    result = (float)num/num2; // 1.666667 
    /*정수끼리 연산하면 소수가 나올 수 없어 (float)캐스팅 연산자를 통해 자료형을 강제로 변환시킨다
    한쪽에 붙이거나 양쪽에 붙이거나 상관없음, 자동 형변환으로 인해 한쪽이 float이면 자동으로 결과값또한 float
    */
    printf("%f \n",result);
    char a = 'A';
    printf("%c \n",a); // 문자 한개 출력
    printf("%d \n",a); // 아스키 코드값 출력
    printf("숫자를 입력하세요 : ");
    int num3;
    scanf("%d",&num3);
    printf("%d \n",num3); //10진수  10000
    printf("%o \n",num3); //8진수 10 000 = 20
    printf("%x \n",num3); //16진수 1 0000 = 10
    
    char *chtest = "ABCDEFG";
    printf("%s \n",chtest);
    /* 메모리 주소를 갖고있는 포인터 변수로 문자열이 저장되어있는 주소를 가리킨다*/

}