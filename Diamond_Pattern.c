#include <stdio.h>
// TC: O(n^2) SC: O(1)
void main() {
    int r,s,count;

    printf("Enter the number of rows:\n");
    scanf("%d", &r);

    count = r - 1;

    // Upper half
    for(int j = 1; j <= r; j++) {
        for(int k = 1; k <=count; k++) {
            printf(" ");
        }
        count--;

        for(int i = 1; i <= 2*j - 1; i++) {
            printf("-");
        }
        printf("\n");
    }

    count = 1;

    // Lower half
    for(int j = 1; j <= r - 1; j++) {
        for(int k = 1; k <= count; k++) {
            printf(" ");
        }
        count++;

        for(int i = 1; i <= 2*(r - j) - 1; i++) {
            printf("-");
        }
        printf("\n");
    }
}