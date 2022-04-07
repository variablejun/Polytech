/*
답변을 입력하세요.
3.컴퓨터와 가위바위보 게임을 하고자 한다. switch문과 if문을 사용하여 다음의 코드의 밑줄부분을 완성하여 제출하시오.
---------------------------------------------------
[실행예시]
[선택하시오 1:가위, 2:바위 3:보 0:게임종료]:  3
비겼습니다
컴퓨터는 "보"입니다.
.....
[선택하시오 1:가위, 2:바위 3:보 0:게임종료]:  2
사용자가 이겼습니다
컴퓨터는 "가위"입니다.
게임횟수는 5이며 승 1, 패 1, 무승부 3회 입니다.
-----------------------------------------------------
*/
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {

	int select, comselect;
	int cntGame, cntWin, cntLose, cntSame;
	cntGame = 0, cntWin = 0, cntLose = 0, cntSame = 0;
	srand(time(NULL));

	
	while (1)
	{
	printf("[선택하시오 1:가위, 2:바위 3:보 0:게임종료]:");
	comselect = rand() % 3 +1;
	cntGame++;
	scanf_s("%d",&select);
		if (select == 0)
			{
				cntGame--;
				printf("게임횟수는 %d이며 승%d, 패%d, 무승부%d회 입니다.\n", cntGame, cntWin, cntLose, cntSame);
				printf("게임을 종료합니다. \n");
				break;
			}
		else if (select>3 || 0>select) {
			printf("0부터 3사이에 값을 입력해주세요. \n");
			cntGame--;
			continue;

		}
		else {
			switch (comselect)
			{

			case 1:
				
				if (select == 1)
				{
					printf("비겼습니다.\n");
					cntSame++;
				}
				else if (select == 2) {
					printf("사용자가 이겼습니다.\n");
					cntWin++;
				}
				else if (select == 3)
				{
					printf("사용자가 졌습니다.\n");
					cntLose++;
				}
				printf("컴퓨터는 \"가위\" 입니다.\n");
				break;

			case 2:
				if (select == 2)
				{
					printf("비겼습니다.\n");
					cntSame++;
				}
				else if (select == 3) {
					printf("사용자가 이겼습니다.\n");
					cntWin++;
				}
				else if (select == 1)
				{
					printf("사용자가 졌습니다.\n");
					cntLose++;
				}
				printf("컴퓨터는 \"바위\" 입니다.\n");
				break;

			case 3:
				if (select == 3)
				{
					printf("비겼습니다.\n");
					cntSame++;
				}
				else if (select == 1) {
					printf("사용자가 이겼습니다.\n");
					cntWin++;
				}
				else if (select == 2)
				{
					printf("사용자가 졌습니다.\n");
					cntLose++;
				}
				printf("컴퓨터는 \"보\" 입니다.\n");
				break;

			}
		}
		
	}//while
	

} //main