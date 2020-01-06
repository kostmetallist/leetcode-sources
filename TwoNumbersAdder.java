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
        }
        return output + ")";
    }
}

public class TwoNumbersAdder {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        return l1;
    }

    public static void main(String[] args) {
        TwoNumbersAdder tna = new TwoNumbersAdder();
        ListNode l1 = new ListNode(2);
        ListNode l1_1 = new ListNode(4);
        ListNode l1_2 = new ListNode(3);
        l1.next = l1_1;
        l1_1.next = l1_2;

        ListNode l2 = new ListNode(5);
        ListNode l2_1 = new ListNode(6);
        ListNode l2_2 = new ListNode(4);
        l2.next = l2_1;
        l2_1.next = l2_2;
        tna.addTwoNumbers(l1, l2);
    }
}
