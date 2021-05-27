# Lowest Common Ancestor of a Binary Tree

[Leetcode problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia:

> The lowest common ancestor is defined between two nodes `p` and `q` as the
> lowest node in `T` that has both `p` and `q` as descendants (where we allow a
> node to be a descendant of itself).


The number of nodes in the tree is in the range `[2, 10^5]`,
`-10^9 <= Node.val <= 10^9`. All `Node.val` are unique. `p != q`, `p` and `q`
are guaranteed to exist in the BST.


## Examples

| Input | Expected Output |
| ----- | --------------- |
| `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]; p = 5; q = 1` | `3` |
| `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]; p = 5; q = 4` | `5` |
| `root = [1, 2]; p = 1; q = 2` | `1` |

## Driver code instructions

```
python driver.py
```
