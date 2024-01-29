from collections import deque
from typing import List

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  2  1  6  7       3
#  1 [3  -1  -3] 2  1  6  7       3
#  1  3 [-1  -3  2] 1  6  7       2
#  1  3  -1 [-3  2  1] 6  7       2
#  1  3  -1  -3 [2  1  6] 7       6
#  1  3  -1  -3  2 [1  6  7]      7


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        index = 0
        window = deque()
        window_max = nums[0]

        while index < k:
            window_max = max(window_max, nums[index])
            window.append(nums[index])
            index += 1

        result = [window_max]

        while index < len(nums):

            next = nums[index]
            last = window.popleft()
            window.append(next)

            if next > window_max:
                window_max = next
            elif last >= window_max:
                window_max = max(window)

            result.append(window_max)
            index += 1

        return result
