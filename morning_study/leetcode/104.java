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
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftDepth = 0;
        int rightDepth = 0;
        
        leftDepth = Math.max(leftDepth, maxDepth(root.left));
        rightDepth = Math.max(rightDepth, maxDepth(root.right));
        
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
