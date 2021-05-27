from typing import List


class Solution:
    def check_ability_to_store(self, height: List[int]) -> bool:
        # returning zero volume in case we have less than two blocks: 
        # valid reservoir can be constructed with at least 3 verticals
        if len(height) < 2:
            return False
        return True

    def trap(self, height: List[int]) -> int:
        if not self.check_ability_to_store(height): 
            return 0

        L      = len(height)
        result = 0
        left_max  = [height[0] for i in range(L)]
        right_max = [height[L-1] for i in range(L)]

        for i in range(1, L-1):
            left_max[i]  = max(left_max[i-1], height[i])
            right_max[L-i-1] = max(right_max[L-i], height[L-i-1])

        for i in range(1, L-1):
            result += min(left_max[i], right_max[i]) - height[i]

        return result
