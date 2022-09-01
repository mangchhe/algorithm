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
    public boolean isPalindrome(ListNode head) {
        StringBuilder sb = new StringBuilder();
        
        while (head != null) {
            sb.append(head.val);
            head = head.next;
        }
        
        String str = sb.toString();
        int total = str.length();
        int cnt = 0;
        
        for (int i = 0; i < total / 2; i++) {
            if (str.charAt(i) == str.charAt(total-i-1)) {
                cnt++;
            }
        }
        
        if (total / 2 == cnt) {
            return true;
        }
        
        return false;
    }
}
