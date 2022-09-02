#include <stdio.h>
int main(){
    char str[30];
    int ch;
    FILE * fp = fopen("simple.txt","rt");
    FILE * des = fopen("des.txt","wt");
    
    if(fp == NULL){
        puts("파일 오픈 실패!");
        return -1;
    }
    while((ch = fgetc(fp)) != EOF){
        fputc(ch, des);
    }

    if(feof(fp) != 0){
        puts("파일복사 완료!");
    }else{
        puts("파일복사 실패!");
    }
    
    /*
    ch = fgetc(fp);
    printf("%c \n", ch);

    ch = fgetc(fp);
    printf("%c \n", ch);
    
    fgets(str, sizeof(str), fp);
    printf("%s", str);

    fgets(str, sizeof(str), fp);
    printf("%s", str);
    */

    fclose(fp);
    fclose(des);
    return 0;
}