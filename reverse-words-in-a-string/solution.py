class Solution:
    def reverseWords(self, s: str) -> str:

        items = s.strip().split()
        items.reverse()
        return ' '.join(items)
