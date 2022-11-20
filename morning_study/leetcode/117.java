/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null)
            return null;
        
        Queue<Node> q = new LinkedList<>();
        q.offer(root);
        
        while (!q.isEmpty()) {
            Queue<Node> tmp = new LinkedList<>();
            
            while (!q.isEmpty()) {
                Node curr = q.poll();
                curr.next = q.peek();
                if (curr.left != null)
                    tmp.offer(curr.left);
                if (curr.right != null)
                    tmp.offer(curr.right);
            }
            q = tmp;
        }
        return root;
    }
}
