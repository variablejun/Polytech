#include <stdio.h>
int main(void){
    int year =0;
    printf("나이를 입력하세요 :");
    scanf("%d",&year);
    printf("%05d 세 입니다. \n",year);
    float cm = 0.0;
    printf("키를 입력하세요 :");
    
    scanf("%f",&cm);
    printf("%-3.2fcm 입니다. \n",cm); // 왼쪽 정렬

    char name[12];
    printf("이름를 입력하세요 :");
    scanf("%s",name);
    printf("%-12s 입니다. \n",name); 

    char gen;
    int num;
    getchar();     
    printf("성별(남성일 경우 m, 여성일 경우 w)과 주민번호 앞자리를 입력하세요 :");
    scanf("%c %d",&gen, &num);
    printf("성별은 %c이고 주민번호는 %d 입니다. \n",gen, num); 
    /*scanf함수가 여러개 있을때 엔터 키가 버퍼에 입력 되어있어 
    제대로 작동하지 않는다 그래서 getchar를 이용해서 버퍼를 비워주어야 제대로 작동한다.*/ 


}