#include <stdio.h>
#define N 20
#define R 2
#define C 3
int main(void) {
	int row, col, total = 0;
	float avg;
	char name[N];
	int st[R][C];

	for (row = 0; row < R; row++) {
		printf("�л� %d�� ����� 3�� ���� ���� �Է�\n", row + 1);
		printf("%d.���� : ", row + 1);

		scanf_s("%s", name, sizeof(name));
		for (col = 0; col < C; col++) {
			printf("����%d ���� : ", col + 1);
			scanf_s("%d", &st[row][col]);
		}
		printf("\n");

		total = st[row][0] + st[row][1] + st[row][2];
		avg = total / 3.0;

		printf("%s�� ���� ��Ȳ\n", name);
		printf("���� : %d\n", total);
		printf("��� : %.2f\n\n", avg);
	}
	printf("��ü %d���� ���� ó�� �� ���α׷� ���� \n", row);
	return 0;
}