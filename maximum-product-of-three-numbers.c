#include <stdio.h>

#define  MAX_SIZE  1024

// Given an integer array, find three numbers whose product 
// is maximum and output the maximum product.

typedef struct {
    int max;
    int avg;
    int min;
} Triplet;

void tripletTryInsertMax(Triplet *triplet, int toInsert) {

    if (toInsert > triplet->min) {

        if (toInsert > triplet->avg) {

            if (toInsert > triplet->max) {

                triplet->min = triplet->avg;
                triplet->avg = triplet->max;
                triplet->max = toInsert;
            }

            else {

                triplet->min = triplet->avg;
                triplet->avg = toInsert;
            }
        }

        else
            triplet->min = toInsert;
    }
}

void tripletTryInsertMin(Triplet *triplet, int toInsert) {

    if (toInsert < triplet->max) {

        if (toInsert < triplet->avg) {

            if (toInsert < triplet->min) {

                triplet->max = triplet->avg;
                triplet->avg = triplet->min;
                triplet->min = toInsert;
            }

            else {

                triplet->max = triplet->avg;
                triplet->avg = toInsert;
            }
        }

        else
            triplet->max = toInsert;
    }
}

int maximumProduct(int *nums, int numsSize) {

    char foundNegative = 0,
        foundNonNegative = 0;
    // TODO negativesMin = {0};
    Triplet negativesMin = {0, 0, 0}, 
        negativesMax = {0, 0, 0}, 
        nonNegativesMax = {0, 0, 0};

    for (int i = 0; i < numsSize; ++i) {

        int value = nums[i];
        if (value >= 0) {

            foundNonNegative = 1;
            tripletTryInsertMax(&nonNegativesMax, value);
        }

        else {

            if (!foundNegative) {

                foundNegative = 1;
                negativesMax.min = value;
                negativesMax.avg = value;
                negativesMax.max = value;
                negativesMin.min = value;
                negativesMin.avg = value;
                negativesMin.max = value;
            }

            else {

                tripletTryInsertMax(&negativesMax, value);
                tripletTryInsertMin(&negativesMin, value);
            }
        }
    }

    if (!foundNegative) 
        return nonNegativesMax.max * nonNegativesMax.avg * nonNegativesMax.min;

    if (!foundNonNegative) 
        return negativesMax.max * negativesMax.avg * negativesMax.min;

    int candidate1 = negativesMin.min * negativesMin.avg * nonNegativesMax.max, 
        candidate2 = nonNegativesMax.min * nonNegativesMax.avg * 
            nonNegativesMax.max;

    return (candidate1 > candidate2)? candidate1: candidate2;
}

int main(int argc, char *argv[]) {

    int array1[MAX_SIZE] = {-4, -3, 0, 1, 2};
    int size1 = 5;

    int array2[MAX_SIZE] = {4, 3, 0, 1, 2};
    int size2 = 5;

    int array3[MAX_SIZE] = {-5, -4, -3, -2, -1};
    int size3 = 5;

    printf("result1 = %d\n", maximumProduct(array1, size1));
    printf("result2 = %d\n", maximumProduct(array2, size2));
    printf("result3 = %d\n", maximumProduct(array3, size3));
    return 0;
}