/*
2.AI기초실습실에서 사용하는 WiFi 번호를 입력하고자 할 때  사용자가 입력하는 번호가 맞는지 확인하는 코드를 작성하시오.

[조건]
1. if 조건문과 scrcmp 함수(문자열 비교함수)를 사용하시오.
2. 번호는 "@Polytech"

[실행예시]
실습실에서 사용하는 WiFi번호를 입력하시오: @polytech
당신이 입력한 번호는 @polytech이며 번호가 틀립니다.

실습실에서 사용하는 WiFi번호를 입력하시오: @Polytech
당신이 입력한 번호는 @Polytech이며 번호가 맞습니다.
*/
#include <stdio.h>
#include <string.h>

int main(void) {
	printf("실습실에서 사용하는 WIFI비밀번호를 입력하시오: ");
	char wifi_num[10] = "@Polytech";
	char wifi_sc[10] = " ";

	int a;
	scanf_s("%s",wifi_sc,sizeof(wifi_sc));

	a = strcmp(wifi_num, wifi_sc); //두 문자열이 같으면 0
	if (a == 0)
	{
		printf("당신이 입력한 번호는 %s이며 번호가 맞습니다.\n",wifi_sc);
	}
	else
	{
		printf("당신이 입력한 번호는 %s이며 번호가 틀립니다.\n", wifi_sc);
	}

}

