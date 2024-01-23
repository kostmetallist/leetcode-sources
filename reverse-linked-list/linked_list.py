from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    val: int = 0
    next: Self = None

    def __str__(self) -> str:

        result = str(self.val)
        elem = self.next
        while elem:
            result += f' -> {elem.val}'
            elem = elem.next

        return result
