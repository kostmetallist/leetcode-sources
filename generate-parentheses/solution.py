from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def recursive(collected, string, left, right):
            if left == right == n:
                collected.append(string)
                return
            if left < n:
                recursive(collected, f'{string}(', left+1, right)
            if left > right:
                recursive(collected, f'{string})', left, right+1)

        result: List[str] = []
        recursive(result, '', 0, 0)
        return result
