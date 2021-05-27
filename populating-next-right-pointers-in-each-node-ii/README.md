# Populating Next Right Pointers in Each Node II

[Leetcode problem](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

## Description

Given a binary tree:

```
struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
}
```

populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to `NULL`. Initially, all next
pointers are set to `NULL`.


The number of nodes in the given tree is less than `6000`;
`-100 <= node.val <= 100`.

Follow up:

- you may only use constant extra space;
- recursive approach is fine, you may assume implicit stack space does not count
as extra space for this problem.

## Examples

| Input | Expected Output |
| ----- | --------------- |
| `root = [1, 2, 3, 4, 5, null, 7]` | `[1, #, 2, 3, #, 4, 5, 7, #]` |

## Driver code instructions

```
javac -cp . *.java
java -cp . Driver
```
