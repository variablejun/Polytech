#include <stdio.h>
#define DT 5


int main(void) {
	int score[DT] = { 88,96,75,81,99 };
	int sum = 0;
	float avg;

	printf("DT 5 \n");
	printf("{ 88,96,75,81,99 } \n");

	sum = sv(score, DT);
	avg = sum / 5.0;

	printf("ÃÑÁ¡ : %d \n", sum);
	printf("Æò±Õ : %.2f \n", avg);
	return 0;

}

int sv(int sc[], int size) {

	int cnt, total = 0;

	for ( cnt = 0; cnt < size; cnt++)
	{
		total += sc[cnt];
	}
	return total;
}