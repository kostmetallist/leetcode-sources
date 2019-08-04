class TreeNode: 
    def __init__(self, x):
        self.val   = x
        self.right = None
        self.left  = None

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
        

######################################################

root = TreeNode(3)
l1n1 = TreeNode(5)
l1n2 = TreeNode(1)
l2n1 = TreeNode(6)
l2n2 = TreeNode(2)
l2n3 = TreeNode(0)
l2n4 = TreeNode(8)
l3n1 = TreeNode(7)
l3n2 = TreeNode(4)

root.left = l1n1
root.right = l1n2
l1n1.left = l2n1
l1n1.right = l2n2
l1n2.left = l2n3
l1n2.right = l2n4
l2n2.left = l3n1
l2n2.right = l3n2

print(Solution().lowestCommonAncestor(root, l3n2, l3n1).val)