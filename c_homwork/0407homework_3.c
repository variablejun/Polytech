/*
�亯�� �Է��ϼ���.
3.��ǻ�Ϳ� ���������� ������ �ϰ��� �Ѵ�. switch���� if���� ����Ͽ� ������ �ڵ��� ���ٺκ��� �ϼ��Ͽ� �����Ͻÿ�.
---------------------------------------------------
[���࿹��]
[�����Ͻÿ� 1:����, 2:���� 3:�� 0:��������]:  3
�����ϴ�
��ǻ�ʹ� "��"�Դϴ�.
.....
[�����Ͻÿ� 1:����, 2:���� 3:�� 0:��������]:  2
����ڰ� �̰���ϴ�
��ǻ�ʹ� "����"�Դϴ�.
����Ƚ���� 5�̸� �� 1, �� 1, ���º� 3ȸ �Դϴ�.
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
	printf("[�����Ͻÿ� 1:����, 2:���� 3:�� 0:��������]:");
	comselect = rand() % 3 +1;
	cntGame++;
	scanf_s("%d",&select);
		if (select == 0)
			{
				cntGame--;
				printf("����Ƚ���� %d�̸� ��%d, ��%d, ���º�%dȸ �Դϴ�.\n", cntGame, cntWin, cntLose, cntSame);
				printf("������ �����մϴ�. \n");
				break;
			}
		else if (select>3 || 0>select) {
			printf("0���� 3���̿� ���� �Է����ּ���. \n");
			cntGame--;
			continue;

		}
		else {
			switch (comselect)
			{

			case 1:
				
				if (select == 1)
				{
					printf("�����ϴ�.\n");
					cntSame++;
				}
				else if (select == 2) {
					printf("����ڰ� �̰���ϴ�.\n");
					cntWin++;
				}
				else if (select == 3)
				{
					printf("����ڰ� �����ϴ�.\n");
					cntLose++;
				}
				printf("��ǻ�ʹ� \"����\" �Դϴ�.\n");
				break;

			case 2:
				if (select == 2)
				{
					printf("�����ϴ�.\n");
					cntSame++;
				}
				else if (select == 3) {
					printf("����ڰ� �̰���ϴ�.\n");
					cntWin++;
				}
				else if (select == 1)
				{
					printf("����ڰ� �����ϴ�.\n");
					cntLose++;
				}
				printf("��ǻ�ʹ� \"����\" �Դϴ�.\n");
				break;

			case 3:
				if (select == 3)
				{
					printf("�����ϴ�.\n");
					cntSame++;
				}
				else if (select == 1) {
					printf("����ڰ� �̰���ϴ�.\n");
					cntWin++;
				}
				else if (select == 2)
				{
					printf("����ڰ� �����ϴ�.\n");
					cntLose++;
				}
				printf("��ǻ�ʹ� \"��\" �Դϴ�.\n");
				break;

			}
		}
		
	}//while
	

} //main