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

    private int diameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        traverse(root);
        return diameter;
    }

    public int traverse(TreeNode curr) {
        if (curr == null) return 0;

        int left = traverse(curr.left);
        int right = traverse(curr.right);

        diameter = Math.max(diameter, left + right);

        return Math.max(left, right) + 1;
    }
}
