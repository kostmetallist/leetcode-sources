# Add Two Promises

[Leetcode problem](https://leetcode.com/problems/add-two-promises/description/)

## Description

Given two promises `promise1` and `promise2`, return a new promise. `promise1` and `promise2` will both resolve with a number. The returned promise should resolve with the sum of the two numbers.

`promise1` and `promise2` are promises that resolve with a number.

## Examples

| Input | Expected Output |
| ----- | --------------- |
| `promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20)), promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60))` | `7` |
| `promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50)), promise2 = new Promise(resolve => setTimeout(() => resolve(-12), 30))` | `-2` |

## Driver code instructions

```
npm start
```
