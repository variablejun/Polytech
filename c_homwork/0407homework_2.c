/*
2.AI���ʽǽ��ǿ��� ����ϴ� WiFi ��ȣ�� �Է��ϰ��� �� ��  ����ڰ� �Է��ϴ� ��ȣ�� �´��� Ȯ���ϴ� �ڵ带 �ۼ��Ͻÿ�.

[����]
1. if ���ǹ��� scrcmp �Լ�(���ڿ� ���Լ�)�� ����Ͻÿ�.
2. ��ȣ�� "@Polytech"

[���࿹��]
�ǽ��ǿ��� ����ϴ� WiFi��ȣ�� �Է��Ͻÿ�: @polytech
����� �Է��� ��ȣ�� @polytech�̸� ��ȣ�� Ʋ���ϴ�.

�ǽ��ǿ��� ����ϴ� WiFi��ȣ�� �Է��Ͻÿ�: @Polytech
����� �Է��� ��ȣ�� @Polytech�̸� ��ȣ�� �½��ϴ�.
*/
#include <stdio.h>
#include <string.h>

int main(void) {
	printf("�ǽ��ǿ��� ����ϴ� WIFI��й�ȣ�� �Է��Ͻÿ�: ");
	char wifi_num[10] = "@Polytech";
	char wifi_sc[10] = " ";

	int a;
	scanf_s("%s",wifi_sc,sizeof(wifi_sc));

	a = strcmp(wifi_num, wifi_sc); //�� ���ڿ��� ������ 0
	if (a == 0)
	{
		printf("����� �Է��� ��ȣ�� %s�̸� ��ȣ�� �½��ϴ�.\n",wifi_sc);
	}
	else
	{
		printf("����� �Է��� ��ȣ�� %s�̸� ��ȣ�� Ʋ���ϴ�.\n", wifi_sc);
	}

}

