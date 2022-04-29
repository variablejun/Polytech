#include <stdio.h>

int main(void) {
    int start;
    int end;

    int temp;
    printf("시작값: ");
    scanf_s("%d", &start);

    printf(" 끝값: ");
    scanf_s("%d", &end);

    if (end > start)
    {
        temp = start;
        start = end;
        end = temp;
    }

    while (1)
    {
        if (start == end)
        {
            break;
        }

        if (start % 2 == 1) {
            printf("%d ", start);
        }

        start--;

    }
  
    return 0;

}