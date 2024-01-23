from collections import deque
from typing import List
from node import Node


class Solution:
    def postorder(self, root: Node) -> List[int]:

        traversed = []
        if not root:
            return traversed

        stack = deque()
        stack.append(root)

        while stack:
            node = stack.pop()
            traversed.append(node.val)
            for child in (node.children or []):
                stack.append(child)

        return list(reversed(traversed))
