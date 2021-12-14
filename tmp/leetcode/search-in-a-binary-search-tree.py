# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        def traverse(node):
            if node == None:
                return None
            if node.val > val:
                return traverse(node.left)
            if node.val < val:
                return traverse(node.right)
            
            return node
        
        return traverse(root)
