#include <stdio.h>
int main(){ 
   FILE * fp = fopen("src2.bin","rb");
    int readDatas[6];
    int readCount = 0;

    if(fp == NULL){
        puts("파일 오픈 실패!");
        return -1;
    }

    readCount = fread(readDatas, sizeof(int), 6, fp);
    for (int i = 0; i < readCount; i++)
    {
        printf("%d \n", readDatas[i]);
    }
    fclose(fp);
    return 0;

}