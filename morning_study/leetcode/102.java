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
        
        List<TreeNode> elements = new ArrayList<TreeNode>();
        elements.add(root);
        List<List<Integer>> res = new ArrayList<>();
        
        while (!elements.isEmpty()) {
            List<Integer> tmp = new ArrayList<>();
            List<TreeNode> next = new ArrayList<>();
            
            for (TreeNode element: elements) {
                tmp.add(element.val);
                if (element.left != null) {
                    next.add(element.left);
                }
                if (element.right != null) {
                    next.add(element.right);   
                }
            }
            elements = next;
            res.add(tmp);
        }
        return res;
    }
}
