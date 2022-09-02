#include <stdio.h>
int main(){ 
    char str[2];
    FILE * fp = fopen("hello.exe","rt");
    FILE * des = fopen("homework.exe","wt");
    
    if(fp == NULL){
        puts("파일 오픈 실패!");
        return -1;
    }

    while(fgets(str, sizeof(char), fp) != NULL){
        fputs(str, des);
    }
    printf("%s", des);
    if(feof(fp) != 0){
        puts("DONE");
    }else{
        puts("FAIL");
    }
}