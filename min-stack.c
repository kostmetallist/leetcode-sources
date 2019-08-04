#include <stdio.h>
#include <stdlib.h>


struct StackElem {

    int value;
    struct StackElem *older;
    struct StackElem *greater;
};

typedef struct {

    int size;
    struct StackElem *head;
    struct StackElem *min;
} MinStack;


MinStack *minStackCreate() {
    
    MinStack *stack = (MinStack *) malloc(sizeof(MinStack));
    stack->size = 0;
    stack->head = NULL;
    stack->min = NULL;
    return stack;
}

void minStackPush(MinStack *obj, int x) {

    struct StackElem *new_elem = (struct StackElem *) malloc(
        sizeof(struct StackElem));
    struct StackElem *min_elem = obj->min;

    new_elem->value = x;
    new_elem->older = obj->head;
    obj->head = new_elem;

    if ((obj->size)++ == 0) {

        new_elem->greater = NULL;
        min_elem = new_elem;
    }

    else if (new_elem->value < min_elem->value) {

        new_elem->greater = min_elem;
        min_elem = new_elem;
    }

    obj->min = min_elem;
}

void minStackPop(MinStack *obj) {

    if (obj->size == 0) 
        return;

    if (obj->head == obj->min)
        obj->min = obj->min->greater;

    struct StackElem *prev = obj->head->older;
    free(obj->head);
    obj->head = prev;
    (obj->size)--;
}

int minStackTop(MinStack *obj) {

    if (obj->size == 0) {

        printf("stack\'s empty\n");
        return -1;
    }

    return obj->head->value;
}

int minStackGetMin(MinStack *obj) {

    if (obj->size == 0) {

        printf("stack\'s empty\n");
        return -1;
    }

    return obj->min->value;
}

void minStackFree(MinStack *obj) {
    
    int cur_size;
    while ((cur_size = obj->size) != 0) {
        minStackPop(obj);
    }

    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, x);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/

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