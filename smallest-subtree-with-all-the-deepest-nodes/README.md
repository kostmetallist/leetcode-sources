# Smallest Subtree with all the Deepest Nodes

[Leetcode problem](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

## Description

Given the `root` of a binary tree, the depth of each node is the shortest
distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the
original tree. A node is called the deepest if it has the largest depth possible
among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all
descendants of that node.


The number of nodes in the tree will be in the range `[1, 500]`.
`0 <= Node.val <= 500`. The values of the nodes in the tree are unique.


**Note**: This question is the same as
[#1123](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/).

## Examples

| Input | Expected Output |
| ----- | --------------- |
| `root = [1]` | `[1]` |
| `root = [0, 1, 3, null, 2]` | `[2]` |
| `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]` | `[2, 7, 4]` |

## Driver code instructions

```
go run solution.go driver.go
```
