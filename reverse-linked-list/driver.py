from random import randint

import solution
from linked_list import ListNode


if __name__ == '__main__':
    s = solution.Solution()

    list_1 = ListNode(1)
    elem = list_1
    for i in range(2, 5+1):
        prev = elem
        elem = ListNode(i)
        prev.next = elem

    print(list_1)
    print(s.reverseList(list_1))

    ###

    list_2 = ListNode(1, ListNode(2))

    print(list_2)
    print(s.reverseList(list_2))

    ###

    list_3 = ListNode(0)
    elem = list_3
    for i in (randint(-5000, 5000) for _ in range(9)):
        prev = elem
        elem = ListNode(i)
        prev.next = elem

    print(list_3)
    print(s.reverseList(list_3))
