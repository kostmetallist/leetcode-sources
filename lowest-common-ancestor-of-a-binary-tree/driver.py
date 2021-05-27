import solution


class TreeNode: 
    def __init__(self, x):
        self.val   = x
        self.right = None
        self.left  = None


if __name__ == '__main__':

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

    print(solution.Solution().lowestCommonAncestor(root, l3n2, l3n1).val)
