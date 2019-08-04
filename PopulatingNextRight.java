// task name: populating-next-right-pointers-in-each-node-ii
// task desc: Given a binary tree, Populate each next pointer to point 
// to its next right node. If there is no next right node, 
// the next pointer should be set to NULL. Initially, all next 
// pointers are set to NULL.
// You may only use constant extra space. Recursive approach is fine, 
// implicit stack space does not count as extra space for this problem.

class Node {

    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val, Node _left, Node _right, Node _next) {

        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}


public class PopulatingNextRight {

    public Node connect(Node root) {

        if (root == null) 
            return root;

        Node baseNode = root;
        Node fantomHead = new Node(0, null, null, null);
        Node pointer = fantomHead;

        while (baseNode != null) {

            if (baseNode.left != null) {

                fantomHead.next = baseNode.left;
                ...
            }
        }

        return root;
    }

    public static void main(String[] args) {

        Node root = new Node(1, null, null, null);
        Node n2 = new Node(2, null, null, null);
        Node n3 = new Node(3, null, null, null);
        Node n4 = new Node(4, null, null, null);
        Node n5 = new Node(5, null, null, null);
        Node n6 = new Node(6, null, null, null);
        Node n7 = new Node(7, null, null, null);

        root.left = n2;
        root.right = n3;
        n2.left = n4;
        n2.right = n5;
        n3.right = n7;
    }
}