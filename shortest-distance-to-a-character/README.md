# Shortest Distance to a Character

[Leetcode problem](https://leetcode.com/problems/shortest-distance-to-a-character/)

## Description

Given a string `s` and a character `c` that occurs in `s`, return an array of
integers `answer` where `answer.length == s.length` and `answer[i]` is the
distance from index `i` to the closest occurrence of character `c` in `s`.

The distance between two indices `i` and `j` is `abs(i - j)`, where `abs` is the
absolute value function.

## Examples

| Input | Expected Output |
| ----- | --------------- |
| `s = "loveleetcode", c = "e"` | `[3,2,1,0,1,0,0,1,2,2,1,0]` |
| `s = "aaab", c = "b"` | `[3,2,1,0]` |
