/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

class Solution {

    public Node connect(Node root) {
                if (root == null)
            return root;

        Node parental = root;
        // specifies beginning of the next tree layer
        Node fantomHead = new Node(0, null, null, null);
        Node ptr = fantomHead;

        while (parental != null) {

            if (parental.left != null) {

                ptr.next = parental.left;
                ptr = parental.left;
            }

            if (parental.right != null) {

                ptr.next = parental.right;
                ptr = parental.right;
            }

            // try to process next non-null node
            if (parental.next != null) 
                parental = parental.next;

            // moving one layer down otherwise
            else {

                parental = fantomHead.next;
                fantomHead = new Node(0, null, null, null);
                ptr = fantomHead;
            }
        }

        return root;
    }
}
