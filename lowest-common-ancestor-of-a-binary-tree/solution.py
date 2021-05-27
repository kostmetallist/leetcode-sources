# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 

    def __init__(self): 
        self.result = None

    def searchKeysSubtrees(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'Boolean':

        if root == None: 
            return False

        found_left, found_right, found_here = False, False, False
        if self.searchKeysSubtrees(root.left, p, q):
            found_left = True

        if self.searchKeysSubtrees(root.right, p, q):
            found_right = True

        if root.val == p.val or root.val == q.val: 
            found_here = True

        if int(found_left) + int(found_right) + int(found_here) >= 2:
            self.result = root

        return found_left or found_right or found_here

    def lowestCommonAncestor(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val and root.val == q.val:
            return root
            
        if self.searchKeysSubtrees(root, p, q):
            return self.result

        else:
            print("Haven't found")
            return None
