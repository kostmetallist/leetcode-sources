# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it is able to trap after raining.

from typing import List

class Solution:
    def check_ability_to_store(self, height: List[int]) -> bool:
        # returning zero volume in case we have less than two blocks: 
        # valid reservoir can be constructed with at least 3 pillars
        if len(height) < 2:
            return False
        return True

    @staticmethod
    def calculate_pool_volume(height: List[int], fr: int) -> int:
        assert fr >= 0, 'Index is not a valid value'
        return 0

    def trap(self, height: List[int]) -> int:
        if not self.check_ability_to_store(height): 
            return 0

        pivot_end  = 0
        second_end = 1
        while second_end < len(height):
            second_end += 1
            pass
        Solution.calculate_pool_volume(height, 0)
        return 0

sol = Solution()
sol.trap([4, 8, 15, 16, 23, 42])