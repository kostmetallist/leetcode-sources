class TreeNode: 
    def __init__(self, x):
        self.val   = x
        self.right = None
        self.left  = None

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

        

######################################################

root = TreeNode(7)
l1n1 = TreeNode(4)
l1n2 = TreeNode(9)
l2n1 = TreeNode(2)
l2n2 = TreeNode(5)
l2n3 = TreeNode(8)
l3n1 = TreeNode(1)
l3n2 = TreeNode(3)

root.left = l1n1
root.right = l1n2
l1n1.left = l2n1
l1n1.right = l2n2
l1n2.left = l2n3
l2n1.left = l3n1
l2n1.right = l3n2

print(Solution().lowestCommonAncestor(root, l2n1, l3n1).val)