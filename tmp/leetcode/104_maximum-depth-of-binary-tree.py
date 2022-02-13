# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        self.ans = 0
        def traverse(node, depth):
            self.ans = max(self.ans, depth)
            if node.left:
                traverse(node.left, depth + 1)
            if node.right:
                traverse(node.right, depth + 1)
                
        if root:
            traverse(root, 1)
        
        return self.ans
        
