#include <stdio.h>
#define R 3
#define C 6

int main(void) {
	int cnt, sno = 203012101; 
	int total = 0;
	float avg;
	int bd[R][C] = {
		{203012101,135,150,148,160,153},
		{203012102,115,120,123,121,112},
		{203012103,132,129,128,133,130}
	};
	printf("고혈압 판정 기준 : 140초과");
	for(cnt= 0;  cnt <R; cnt++)
	{
		total = bd[cnt][1] + bd[cnt][2] + bd[cnt][3] + bd[cnt][4]+ bd[cnt][5];

		avg = total / 5.0;
		printf("\n 환자 #%d의 수축기 평균 혈압 및 판정\n", cnt + 1);
		printf("번호 : %d \n", bd[cnt][0]);
		printf("혈압 : %.2f\n", avg);

		if (avg > 140)
		{
			printf("판정 : 고혈압\n");
		}
		else
		{
			printf("판정 : 정상\n");
		}
	}
	return 0;
}