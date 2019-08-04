#include <stdio.h>
#include <stdlib.h>

#define  INT_SIZE sizeof(int)

// Returns a new integer array res[returnSize] containing 
// in res[i] product of all nums[j] for all j except i.
// Note: assuming numsSize > 1.
// Note: result array is malloced inside.
int *productExceptSelf(int *nums, int numsSize, int *returnSize) {

    // allocating arrays for left and right multiplication
    int *leftSide = (int *) calloc(numsSize, INT_SIZE), 
        *rightSide = (int *) calloc(numsSize, INT_SIZE), 
        *result = (int *) calloc(numsSize, INT_SIZE);

    leftSide[0] = rightSide[numsSize-1] = 1;
    for (int i = 1; i < numsSize; ++i) {
        leftSide[i] = leftSide[i-1] * nums[i-1];
        rightSide[numsSize-1-i] = rightSide[numsSize-i] * nums[numsSize-i];
    }

    for (int i = 0; i < numsSize; ++i) {
        result[i] = leftSide[i] * rightSide[i];
    }

    free(leftSide);
    free(rightSide);
    *returnSize = numsSize;
    return result;
}

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