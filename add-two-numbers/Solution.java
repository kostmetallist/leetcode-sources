/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
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

        }

        if (carry_value != 0) {
            ListNode tmp = new ListNode(carry_value);
            curr.next = tmp;
        }

        return output;
    }
}
