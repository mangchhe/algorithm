/**
 * url : https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2){

        int carry = 0;
        ListNode result = new ListNode();
        ListNode current;
        current = result;

        while(l1 != null || l2 != null){

            current.next = new ListNode();
            current = current.next;

            if(l1 != null){
                carry += l1.val;
                l1 = l1.next;
            }

            if(l2 != null){
                carry += l2.val;
                l2 = l2.next;
            }

            current.val = carry % 10;
            carry /= 10;

        }
        if(carry > 0){
            current.next = new ListNode(1);
        }
        return result.next;
    }

    public static void main(String[] args) {

    }
}

class ListNode {
    int val;
    ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }


    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}