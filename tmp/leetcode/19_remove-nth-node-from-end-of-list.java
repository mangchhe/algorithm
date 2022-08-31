/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int total = 0;
        ListNode curr = head;
        while (curr != null) {
            curr = curr.next;
            total++;
        }
        
        ListNode start = new ListNode(0, head);
        curr = head;
        
        for (int i = 0; i < total - n - 1; i++) {
            curr = curr.next;
        }
        
        if (total == 1 && n == 1) {
            return null;
        }
        
        if (n == 1) {
            curr.next = null;
            return start.next;
        }
        
        if (total - n == 0) {
            start.next = curr.next;
            return start.next;
        }
        
        curr.next = curr.next.next;
        return start.next;
    }
}
