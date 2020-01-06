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

public class TwoNumbersAdder {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        int carry_value = 0;
        ListNode n1 = l1, n2 = l2;
        ListNode output = null;
        ListNode curr = output;
        do {
            if (curr == null) {
                curr = new ListNode(0);
                output = curr;
            } else {
                ListNode tmp = new ListNode(carry_value);
                curr.next = tmp;
                curr = tmp;
            }

            curr.val += n1.val + n2.val;
            carry_value = curr.val / 10;
            curr.val %= 10;
            n1 = n1.next;
            n2 = n2.next;
        } while (n1 != null && n2 != null);

        if (n1 == null && n2 != null) {
            while (n2 != null) {
                ListNode tmp = new ListNode(carry_value);
                curr.next = tmp;
                curr = tmp;
                curr.val += n2.val;
                carry_value = curr.val / 10;
                curr.val %= 10;
                n2 = n2.next;
            }

        } else if (n1 != null && n2 == null) {
            while (n1 != null) {
                ListNode tmp = new ListNode(carry_value);
                curr.next = tmp;
                curr = tmp;
                curr.val += n1.val;
                carry_value = curr.val / 10;
                curr.val %= 10;
                n1 = n1.next;
            }

        } else {
            if (carry_value != 0) {
                ListNode tmp = new ListNode(carry_value);
                curr.next = tmp;
            }
        }

        return output;
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
        ListNode l2_3 = new ListNode(5);
        l2.next = l2_1;
        l2_1.next = l2_2;
        l2_2.next = l2_3;

        System.out.println(l1);
        System.out.println(l2);
        ListNode result = tna.addTwoNumbers(l1, l2);
        System.out.println(result);
    }
}
