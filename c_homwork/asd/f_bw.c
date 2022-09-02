#include <stdio.h>
int main(){
    /*
    과제 pdf 학번_이름.pdf.
    소스코드 결과 나의 고찰
    25page

    exe 파일을 복사해서 실행을 시켜보기(hello world)

 */
    FILE * fp = fopen("src2.bin","wb");
    int myDatas[6] = {0,1,2,3,4,5};

    if(fp == NULL){
        puts("파일 오픈 실패!");
        return -1;
    }
    fwrite((void *)myDatas, sizeof(int), 6, fp);
   

 
}
