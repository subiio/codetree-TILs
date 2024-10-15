#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int a =5, b=6,c=7;
    int temp1, temp2;
    temp1 = a;
    a = c;
    temp2 = b;
    b = temp1;
    c = temp2;

    printf("%d\n%d\n%d",a,b,c);
    return 0;
}