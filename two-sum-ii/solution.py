from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        # Not considering "==" case due to `You may not use the same element twice`
        while lo < hi:
            if (candidate := numbers[lo] + numbers[hi]) == target:
                # We can freely rely on a constraint that a solution 
                # is guaranteed to exist.
                break
            elif candidate < target:
                lo += 1
            else:
                hi -= 1

        # +1 as the problem requires to return numbers not indices 🤷                
        return [lo + 1, hi + 1]
