#include <stdio.h>
#include "solution.c"


int main(int argc, char **argv) {

    MinStack *obj = minStackCreate();


    minStackPush(obj, -2);
    minStackPush(obj, 0);
    minStackPush(obj, -3);

    printf("min: %d\n", minStackGetMin(obj));
    minStackPop(obj);
    printf("top: %d\n", minStackTop(obj));
    printf("min: %d\n", minStackGetMin(obj));


    minStackFree(obj);
    return 0;
}
