/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null)
            return List.of();
        
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        
        while (!q.isEmpty()) {
            Deque<TreeNode> tmp = new ArrayDeque<>();
            res.add(q.peekLast().val);
        
            while (!q.isEmpty()) {
                TreeNode curr = q.poll();
                if (curr.left != null)
                    tmp.offer(curr.left);
                if (curr.right != null)
                    tmp.offer(curr.right);
            }
            q = tmp;
        }
        return res;
    }
}
