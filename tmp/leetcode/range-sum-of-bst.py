# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans = 0
    def rangeSumBST(self, root, low, high):
        def traverse(node):
            if low <= node.val <= high:
                self.ans += node.val
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
                
        traverse(root)
        
        return self.ans
