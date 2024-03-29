# Sliding Window Maximum

[Leetcode problem](https://leetcode.com/problems/sliding-window-maximum/description/)

## Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Examples

| Input | Expected Output |
| ----- | --------------- |
| `nums = [1,3,-1,-3,5,3,6,7], k = 3` | `[3,3,5,5,6,7]` |
| `nums = [1], k = 1"` | `[1]` |
