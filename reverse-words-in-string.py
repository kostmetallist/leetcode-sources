class Solution:
    def reverseWords(self, s: str) -> str:

        items = s.strip().split()
        items.reverse()
        return ' '.join(items)


testStr1 = "the sky is blue"
testStr2 = "  hello world!  "
testStr3 = "a good   example"
solution = Solution()

print(solution.reverseWords(testStr1))
print(solution.reverseWords(testStr2))
print(solution.reverseWords(testStr3))