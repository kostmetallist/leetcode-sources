from collections import deque
from dataclasses import dataclass
from typing import List

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  2  1  6  7       3
#  1 [3  -1  -3] 2  1  6  7       3
#  1  3 [-1  -3  2] 1  6  7       2
#  1  3  -1 [-3  2  1] 6  7       2
#  1  3  -1  -3 [2  1  6] 7       6
#  1  3  -1  -3  2 [1  6  7]      7


@dataclass
class Candidate:
    value: int
    index: int


class Solution:

    def add_candidate(self, candidates: deque[Candidate], insertee: Candidate, cut_index: int = 0):

        while candidates and candidates[-1].value < insertee.value:
            candidates.pop()
        
        if candidates and candidates[0].index < cut_index:
            candidates.popleft()

        candidates.append(insertee)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        index = 0
        candidates = deque()
        result = []

        while index < k:
            self.add_candidate(candidates, Candidate(nums[index], index))
            # print(f'{index=}; {' '.join(str(x.value) for x in candidates)}')
            index += 1

        result.append(candidates[0].value)

        while index < len(nums):
            self.add_candidate(candidates, Candidate(nums[index], index), index - k + 1)
            # print(f'{index=}; {' '.join(str(x.value) for x in candidates)}')
            result.append(candidates[0].value)
            index += 1

        return result
