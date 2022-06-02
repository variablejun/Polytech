#include <stdio.h>
#define AL 8
int b_s(int list[], int n, int input);
/*선택정렬

가장맨앞에 데이터중 가장 작은 값을 찾아 교환해 가며 정렬
1회전시 무조건 제일 작은데이터가 앞으로 온다
그 뒤로 회전 시 마다 하나씩 정렬
*/
int solt(int s_list[]) {
	int a, b, temp, sort;
	for (a = 0; a < AL - 1; a++) { // 0번째 방부터 배열-1번째 방까지 반복
			sort = a; // sort에 a 대입
			for (b = a + 1; b < AL; b++) // 1번째 방부터(a + 1) 배열 끝방까지 반복
			{
			// 1회전 시 첫번째방에 무조건 가장 작은게 들어가서 비교할 이유가 없다.
			
				if (s_list[b] < s_list[sort]) { // n 자리가 n+1 자리보다 클때
					// 그 방의 인덱스를 sort에 대입하여 sort가 회전시 
					// 가장 작은 방을 가리키는 인덱스로 남게함
					sort = b;
				}
			}
			// 가장 작은 방을 가리키게된 sort는 sort가 가진 값을 현재 첫번째 방 인덱스를 가진
			// a에 대입되어  1회전시 가장 작은 값이 첫번째 방으로 오게 되고 반복
			// 임시 버퍼를 통해 자리를 바꾸는 것
			temp = s_list[a];
			s_list[a] = s_list[sort];
			s_list[sort] = temp;

		}
	printf("결과 배열요소 : ");
		for (a = 0; a < AL; a++)
		{
			printf("%d ->", s_list[a]);
		}
}

int main(void) {
	int s_list[AL] = { 15,24,35,3,8,57,68,85 };

	printf("초기 15,24,35,3,8,57,68,85 \n");
	printf("\n[for 문으로 선택 정렬 수행]\n");	
	solt(s_list);

	int input, search;
	char yn;

	do {
		printf("숫자 입력 : ");
		scanf_s("%d", &input);

		search = b_s(s_list, AL, input);
		printf("탐색 성공 인덱스 : [%2d] \n", search);

	re_input:
		printf("프로그램 재실행 (Y/N) : ");
		scanf_s(" %c", &yn, sizeof(yn));

		if (yn == 'N' || yn == 'n')
		{
			break;
		}
		else if (yn == 'Y' || yn == 'y') {
			continue;
		}
		else {
			printf("\n 알파벳 입력 오류! \n");
			printf("알파벳을 다시 입려하세요. \n");
			goto re_input;

		}
	}while (1); // 

	return 0;
}
/*이진 탐색

찾는 값을 배열 중간부터 탐색하는 방법, 
배열 요소를 두부분으로 나누어 찾는것, 무조건 순서대로 정렬이 되어있어야 한다
중간값을 기준으로 적으면 한칸아래로 high를 조정, 크면 한칸 위로 low를 조절
그리고 다시 중간값(인덱스)를 조절해 나가다 사용자가 입력한 값을 중간값이 가리키면 리턴해주고 종료

정렬된 리스트, 선언된 배열크기, 사용자가 찾을값
*/
int b_s(int list[], int n, int input) {
	int low = 0; // 하한값 대입 변수
	int high = n - 1; // 상한값 대입 변수 -1은 0 ~ 7 이기 때문에 8이 들어오면 검색 불가
	// 정렬된 배열에서 가장 큰값을 넣어주기 위한 것
	int md, cnt = 1; //중간값과 카운트 변수
	
	while (low <= high) { // 검색해 가며 남아있는 배열요소가 없어질 때 까지 수행

		printf("%d회 이진 탐색 : [%d %d]\n", cnt, low, high);
		md = (low + high) / 2; // 중간 위치를 산출하여 미들값에 대입
		// if문을 통해 low/high값이 재정의 되면 다시 거기서 나누어서 새로운 중간값을 찾는다
		// 여기서 중간값은 배열의 값이 아닌 인덱스 번호를 말한다,
		if (input == list[md]) // 사용자가 찾을 값과 md가 가리키는 값이 같으면 값 반환
		{
			return md; // 찾은값 반환
		}
		else if (input > list[md]) { 
			low = md + 1; // 사용자가 입력한 값이 중간값보다 크면 중간값 다음 인덱스를
			// low에 대입
		}
		else {
			high = md - 1;
			// 중간값이 작으면 중간값 - 1 인덱스를 high에 대입
		}
		cnt++;
	}
	return -1;
}