# Merge Intervals

[Leetcode problem](https://leetcode.com/problems/merge-intervals/description/)

## Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Examples

| Input | Expected Output |
| ----- | --------------- |
| `intervals = [[1,3],[2,6],[8,10],[15,18]]` | `[[1,6],[8,10],[15,18]]` |
| `intervals = [[1,4],[4,5]]` | `[[1,5]]` |
