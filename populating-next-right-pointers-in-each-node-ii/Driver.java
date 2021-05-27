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

public class Driver {
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

        // Actually, no solution check here - TODO?
    }
}
