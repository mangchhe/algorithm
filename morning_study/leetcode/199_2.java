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
        List<Integer> res = new ArrayList<>();
        traverse(res, root, 0);
        return res;
    }
    
    private void traverse(List<Integer> res, TreeNode curr, int depth) {
        if (curr == null)
            return;
        
        if (res.size() == depth) {
            res.add(curr.val);
        }
        
        traverse(res, curr.right, depth + 1);
        traverse(res, curr.left, depth + 1);
    }
}
