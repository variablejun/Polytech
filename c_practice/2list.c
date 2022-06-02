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
		printf("학생 %d의 성명과 3개 과목 점수 입력\n", row + 1);
		printf("%d.성명 : ", row + 1);

		scanf_s("%s", name, sizeof(name));
		for (col = 0; col < C; col++) {
			printf("과목%d 점수 : ", col + 1);
			scanf_s("%d", &st[row][col]);
		}
		printf("\n");

		total = st[row][0] + st[row][1] + st[row][2];
		avg = total / 3.0;

		printf("%s의 성적 현황\n", name);
		printf("총점 : %d\n", total);
		printf("평균 : %.2f\n\n", avg);
	}
	printf("전체 %d명의 성적 처리 후 프로그램 종료 \n", row);
	return 0;
}