/*1.�� ���� ������ �Է��Ͽ� ���� ū ���� ���� ���� ���� ����ϴ� �ڵ带 �ۼ��Ͻÿ�.
[����]
scanf_s�Լ��� if ���ǹ��� �ݵ�� Ȱ���Ͻÿ�.

[��¿���]
�� ���� ������ �Է��Ͻÿ�:1 3  5
������ ���� �� ���� ū���� 5, ���� �������� 1 �Դϴ�.*/

#include <stdio.h>

int main(void) {
	int num1, num2, num3,max, min;
	printf("�� ���� ������ �Է��Ͻÿ�: ");
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
		printf("������ ���� �� ���� ū���� %d, ���� ���� ���� %d �Դϴ�.", max, min);
	}
	else
	{
		printf("0�̻��� ������ �Է��� �ּ���.\n");
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