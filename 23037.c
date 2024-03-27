//chatgpt 참고
#include <stdio.h>

int main() {
    int input, sum = 0;
    scanf("%d", &input);

    while (input > 0) {
        int digit = input % 10; // 현재 자릿수를 구함
        sum += digit * digit * digit * digit * digit; // 각 자릿수를 5번 곱하여 더함
        input /= 10; // 다음 자릿수로 이동
    }

    printf("%d", sum);
    return 0;
}
