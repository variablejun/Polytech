#include <stdio.h>

int a;
static int b;

void in_fun(void);
extern void out_fun(void);

int main(void) {
    printf("���� ������ �ܺ� ���� �Լ� ȣ��\n");
    printf("Ű���� ��� extern \n");

    out_fun();
    printf("1. �ܺ� ���ᰪ ��� %d \n", a);
    printf("���� ���� ���� ���� ���� �Լ� ȣ��");
    printf("Ű���� ��� static \n");

    in_fun();
    printf("2. �ܺ� ���� �Լ����� �� ��� %d \n", b);

}

void in_fun(void) {
    b = 20;
    printf("\n [���� in_fun() �Լ� ����] \n");
}