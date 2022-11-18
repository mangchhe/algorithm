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
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        int res = traverse(root, 0);
        return res < 0 ? false : true;
    }
    
    public int traverse(TreeNode node, int depth) {
        if (node == null)
            return depth - 1;
            
        int leftDepth = traverse(node.left, depth + 1);
        int rightDepth = traverse(node.right, depth + 1);
        
        if (Math.abs(leftDepth - rightDepth) > 1) {
            return -9999999;
        }
        
        return Math.max(leftDepth, rightDepth);
    }
}
