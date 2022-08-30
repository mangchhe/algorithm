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
    public ListNode deleteMiddle(ListNode head) {
        ListNode cur = head;
        int cnt = 0;
        while (cur != null) {
            cur = cur.next;
            cnt++;
        }
        
        if (cnt == 1) {
            head = null;
            return head;
        }
        else if (cnt == 2) {
            head.next = null;
            return head;
        }
        
        int middle = cnt / 2;
        
        cnt = 0;
        ListNode start = new ListNode(0, head);
        ListNode prev = start;
        cur = head;
        
        while (cur != null) {
            if (cnt++ != middle) {
                prev.next = cur;
                prev = cur;
            } 
            cur = cur.next;
        }
        
        return start.next;
    }
}
