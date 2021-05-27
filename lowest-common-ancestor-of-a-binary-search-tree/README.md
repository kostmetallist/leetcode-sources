# Lowest Common Ancestor of a Binary Search Tree

[Leetcode problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

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
| `root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]; p = 2; q = 8` | `6` |
| `root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]; p = 2; q = 4` | `2` |
| `root = [2, 1]; p = 2; q = 1` | `2` |

## Driver code instructions

```
python driver.py
```
