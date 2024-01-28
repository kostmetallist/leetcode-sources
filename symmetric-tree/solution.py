from collections import deque
from typing import Optional
from tree_node import TreeNode


class Solution:

    def _get_traversal(self, root: Optional[TreeNode], left_to_right=True) -> [int]:

        traversal = []
        if not root:
            return traversal

        stack = deque([root])

        while stack:
            node = stack.pop()
            if not node:
                traversal.append(None)
                continue

            traversal.append(node.val)

            if left_to_right:
                stack.append(node.right)
                stack.append(node.left)
            else:
                stack.append(node.left)
                stack.append(node.right)

        return traversal

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self._get_traversal(root.left) == self._get_traversal(root.right, False)
