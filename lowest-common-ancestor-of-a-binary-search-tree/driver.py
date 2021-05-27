import solution


class TreeNode: 
    def __init__(self, x):
        self.val   = x
        self.right = None
        self.left  = None


if __name__ == '__main__':

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

    print(solution.Solution().lowestCommonAncestor(root, l2n1, l3n1).val)
