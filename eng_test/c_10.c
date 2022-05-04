#include <stdio.h>
struct Soojebi
{
    char name[10];
    int age;
};

int main(){
    struct Soojebi s[]={
        "Kim", 28, "Lee",38 ,"Seo", 50, "Park", 35
    };
    struct Soojebi *p; //구조체 포인터 타입 변수
    p = s; // 수제비 구조체로 선언된 s변수의 주소값을 대입한다 
    p++; // p안에 들어있는 s의 주소값을 1 더해준다 
    //s는 이름 자체로 &선언 없이도 메모리 첫번째를 가리킨다 즉 kim 28 을 가리키고있다.
    //거기에 1을 더하면 다음 방인 lee 38 을 가리키게된다
    printf("%s \n", p->name);
    printf("%d \n", p->age);

    
}
/*
Lee 
38 
*/