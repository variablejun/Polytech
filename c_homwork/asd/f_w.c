#include <stdio.h>
int main(){
    FILE * fp = fopen("simple.txt","wt");
    // fopen 파일과 스트림형성
    // fopen("파일 이름","형성할 스트림의 종류")
    // FILE 구조체 변수 생성
    // FILE 구조체의 포인터 변수는 파일을 가리키는 지시자 역할
    if(fp == NULL){
        puts("파일 오픈 실패!");
        return -1;
    }
    fputc('A',fp);
    fputc('B',fp);
    fputs("MY name is jun \n", fp);
    fputs("your name is jeon \n", fp);
    fclose(fp);
    // open된 파일의 스트림을 종료
    return 0;
}