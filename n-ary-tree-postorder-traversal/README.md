# N-ary Tree Postorder Traversal

[Leetcode problem](https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/)

## Description

Given the `root` of an n-ary tree, return the postorder traversal of its nodes' values.

N-ary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `0 <= Node.val <= 10^4`
- The height of the n-ary tree is less than or equal to `1000`.


## Examples

| Input | Expected Output |
| ----- | --------------- |
| `root = [1,null,3,2,4,null,5,6]` | `[5,6,3,2,4,1]` |
| `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]` | `[2,6,14,11,7,3,12,8,4,13,9,10,5,1]` |