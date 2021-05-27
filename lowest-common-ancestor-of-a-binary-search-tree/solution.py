# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Note: this task states to work with Binary Search Tree, thus programmer 
# can rely on such data structure features including basic property of BST: 
# every node on the left side must have less or equal key value.
class Solution: 
    def lowestCommonAncestor(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root
