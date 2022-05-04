#include <stdio.h>
struct Soojebi
{
    char name[20];
    int os, db, hab1, hab2;
};

int main(){
    struct Soojebi s[3] = {
        {"데이터1", 95, 88},
        {"데이터2", 84, 91},
        {"데이터3", 86, 75}
    }; //합은 초기화 되지 않은상태 존재는한다.
    struct Soojebi *p;

    p = &s[0];
    (p+1) -> hab1 = (p+1)->os+(p+2)->db; // 84 + 75 = 159 2번째에 os 값과 3번째의 db 값
    (p+1) -> hab2 = (p+1)->hab1+ p->os + p->db; // 159 + 95 + 98 =342  첫번째 os db값과 위 코드로 초기화된 hap1 값 더하여 2번째 hap2에 대입

    printf("%d \n", (p+1)->hab1 + (p+1)->hab2); // 159 + 342 = 501 
    
}
//501 