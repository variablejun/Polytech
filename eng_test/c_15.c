#include <stdio.h>
int main(){
    int *arr[3];
    int a = 12, b = 24, c = 36;
    arr[0] = &a; //변수의 주소값을 포인터 배열에 삽입
    arr[1] = &b;
    arr[2] = &c;
    
    printf("%d \n", *arr[1] + **arr + 1); // *arr[1] 1번방에 있는 주소값 즉24를 말하고 
    //**arr + 1 *arr는 arr[0]와 같고 그것의 값을 가져오기 위해 *을 하나 더 붙였다 그래서 12를 가져오고 +1 한다
    //그 둘을 합쳐 37이 나온다. 
}
//37 