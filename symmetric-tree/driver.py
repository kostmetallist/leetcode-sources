from tree_node import TreeNode
import solution


if __name__ == '__main__':

    s = solution.Solution()

    root = TreeNode(1)

    l1n1 = TreeNode(2)
    l1n2 = TreeNode(2)
    root.left = l1n1
    root.right = l1n2

    l2n1 = TreeNode(3)
    l2n2 = TreeNode(4)
    l2n3 = TreeNode(4)
    l2n4 = TreeNode(3)
    l1n1.left = l2n1
    l1n1.right = l2n2
    l1n2.left = l2n3
    l1n2.right = l2n4

    print(s.isSymmetric(root))

    # ---

    root = TreeNode(1)

    l1n1 = TreeNode(2)
    l1n2 = TreeNode(2)
    root.left = l1n1
    root.right = l1n2

    l2n1 = TreeNode(3)
    l2n2 = TreeNode(3)
    l1n1.right = l2n1
    l1n2.right = l2n2

    print(s.isSymmetric(root))
