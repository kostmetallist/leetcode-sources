from typing import Optional
from linked_list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        # Thought process and naming as if we're scanning the list left to right
        left = head
        curr = left.next
        left.next = None

        while curr:
            right = curr.next
            curr.next = left
            left = curr
            curr = right

        return left
