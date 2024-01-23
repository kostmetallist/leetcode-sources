from node import Node
from solution import Solution


if __name__ == '__main__':
    s = Solution()

    root = Node(1)

    # Layer 1 number 1
    l1n1 = Node(2)

    l1n2 = Node(3)
    l1n3 = Node(4)
    l1n4 = Node(5)

    root.children = [
        l1n1,
        l1n2,
        l1n3,
        l1n4,
    ]

    l2n1 = Node(6)
    l2n2 = Node(7)
    l2n3 = Node(8)
    l2n4 = Node(9)
    l2n5 = Node(10)

    l1n2.children = [
        l2n1,
        l2n2,
    ]
    
    l1n3.children = [l2n3]
    l1n4.children = [
        l2n4,
        l2n5,
    ]

    l3n1 = Node(11)
    l3n2 = Node(12)
    l3n3 = Node(13)

    l2n2.children = [l3n1]
    l2n3.children = [l3n2]
    l2n4.children = [l3n3]

    l4n1 = Node(14)

    l3n1.children = [l4n1]

    print(s.postorder(root))
