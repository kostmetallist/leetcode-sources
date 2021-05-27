class ListNode {
    int val;
    ListNode next;

    ListNode(int x) { 
        val = x;
    }

    @Override
    public String toString() {

        String output = "( ";
        ListNode curr = this;
        while (curr != null) {
            output += curr.val + " ";
            curr = curr.next;
        }
        return output + ")";
    }
}

public class Driver {
    public static void main(String[] args) {

        Solution tna = new Solution();
        ListNode l1 = new ListNode(2);
        ListNode l1_1 = new ListNode(4);
        ListNode l1_2 = new ListNode(3);
        l1.next = l1_1;
        l1_1.next = l1_2;

        ListNode l2 = new ListNode(5);
        ListNode l2_1 = new ListNode(6);
        ListNode l2_2 = new ListNode(4);
        ListNode l2_3 = new ListNode(5);
        l2.next = l2_1;
        l2_1.next = l2_2;
        l2_2.next = l2_3;

        ListNode l3 = new ListNode(9);
        ListNode l3_1 = new ListNode(9);
        l3.next = l3_1;

        ListNode l4 = new ListNode(1);

        System.out.println(l3);
        System.out.println(l4);
        ListNode result = tna.addTwoNumbers(l3, l4);
        System.out.println(result);
    }    
}
