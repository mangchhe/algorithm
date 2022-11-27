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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<List<Integer>> res = new ArrayList<>();
        traverse(res, root, 0);
        return res;
    }
    
    private void traverse(List<List<Integer>> res, TreeNode curr, int level) {
        if (res.size() <= level) {
            res.add(new ArrayList<>());
        }
        
        res.get(level).add(curr.val);
        
        if (curr.left != null) traverse(res, curr.left, level + 1);
        if (curr.right != null) traverse(res, curr.right, level + 1);
    }
}
