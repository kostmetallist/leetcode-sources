from typing import List
import bisect

# nums = [10,9,2,5,3,7,101,18]
#              _ _   _ ___     => 4
#              _   _ _ ___     => also 4


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
