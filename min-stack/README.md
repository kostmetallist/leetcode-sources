# Min Stack

[Leetcode problem](https://leetcode.com/problems/min-stack/)

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the `MinStack` class/struct:

- `MinStack()` initializes the stack object;
- `void push(val)` pushes the element val onto the stack;
- `void pop()` removes the element on the top of the stack;
- `int top()` gets the top element of the stack;
- `int getMin()` retrieves the minimum element in the stack.

`-2^31 <= val <= 2^31 - 1`.

Operations `pop`, `top` and `getMin` will always be called on non-empty stacks.
At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## Examples

**Input**:

- `["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]`
- `[[],         [-2],   [0],    [-3],   [],       [],    [],    []]`

**Expected Output**:

- `[null,       null,   null,   null,   -3,       null,  0,     -2]`

## Driver code instructions

```
gcc -c solution.c driver.c
gcc driver.o
./a.out
```
