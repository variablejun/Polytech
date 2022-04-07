/*1.세 개의 정수를 입력하여 제일 큰 수와 제일 작은 수를 출력하는 코드를 작성하시오.
[조건]
scanf_s함수와 if 조건문을 반드시 활용하시오.

[출력예시]
세 개의 정수를 입력하시오:1 3  5
세개의 정수 중 가장 큰수는 5, 가장 작은수는 1 입니다.*/

#include <stdio.h>

int main(void) {
	int num1, num2, num3,max, min;
	printf("세 개의 정수를 입력하시오: ");
	scanf_s("%d %d %d",&num1,&num2,&num3);
	if (num1 >= 0 && num2 >= 0 && num3 >= 0)
	{
		if (num1 >= num2)
		{
			max = num1;
		}
		else
		{
			max = num2;
		}
		if (num3 >= max)
		{
			max = num3;
		}

		if (num1 >= num2)
		{
			min = num2;
		}
		else
		{
			min = num1;
		}
		if (min >= num3)
		{
			min = num3;
		}
		printf("세개의 정수 중 가장 큰수는 %d, 가장 작은 수는 %d 입니다.", max, min);
	}
	else
	{
		printf("0이상의 정수를 입력해 주세요.\n");
	}
	
	
}

/*
int num_max(num1, num2, num3) {
	int max;
	if (num1 >= num2)
	{
		max = num1;
	}
	else
	{
		max = num2;
	}
	if (num3 >= max)
	{
		max = num3;
	}
	return max;
}

int num_min(num1, num2, num3) {
	int min;
	if (num1 >= num2)
	{
		min = num2;
	}
	else
	{
		min = num1;
	}
	if (min >= num3)
	{
		min = num3;
	}
	return min;
}*/