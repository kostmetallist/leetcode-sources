#include <stdio.h>
#include <stdlib.h>
#include "solution.c"


int main(int argc, char *argv[]) {

    int input[] = {1, 2, 3, 4};
    int returnSize;
    int *result = productExceptSelf(input, 4, &returnSize);

    printf("result:\n");
    for (int i = 0; i < returnSize; ++i) {
        printf("%d ", result[i]);
    }

    printf("\n");
    free(result);
    return 0;
}
