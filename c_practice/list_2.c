#include <stdio.h>
#define CP 10

int main(void) {
	char yn;
	int choice, cnt;

	int car[CP] = { 0 };

	do
	{
		printf("�ڵ��� ���� �����Ͻðڽ��ϱ�? (Y/N) : ");
		scanf_s(" %c", &yn, sizeof(yn));
		if (yn == 'N' || yn == 'n')
		{
			break;
		}
		else if (yn == 'Y' || yn == 'y')
		{
			printf("�ڵ��� �� ��ȣ : 1 2 3 4 5 6 7 8 9 10 \n");
			printf("�ڵ��� ���� ��Ȳ : ");
			for ( cnt = 0; cnt < CP; cnt++)
			{
				printf("%2d", car[cnt]);
			}
			printf("\n");
			
		re_input:
			printf("\n �ڵ��� �� ����(1 ~ 10) : ");
			scanf_s("%d", &choice);

			if (choice < 1 || choice > 10)
			{
				printf("�߸� �Է��߽��ϴ�. \n");
				printf("�� ��ȣ�� �ٽ� �Է��ϼ���. \n");
				goto re_input;
			}
			else {
				if (car[choice -1] == 0)
				{
					car[choice - 1] = 1;
					printf("���� �Ϸ�! \n");
				}
				else
				{
					printf("[No.%d] ���� �̹� ����Ǿ����ϴ�.\n",choice);
					printf("�� ��ȣ�� �ٽ� �����ϼ���. \n");
					goto re_input;
				}
			}
		}
		else {
			printf("���ĺ� �Է� ����! \n");
			printf("���ĺ��� ��ҹ��� �������� Y �Ǵ� N�� ����մϴ�. \n");
			printf("���ĺ��� �ٽ� �Է��Ͻÿ�.\n\n");
		}

	} while (1);
	printf("�ڵ��� �� [No.%d] ���� �Ϸ� �� ���α׷� ���� \n", choice);
	return 0;
}
