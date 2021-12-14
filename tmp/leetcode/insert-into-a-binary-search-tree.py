# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        def insert(parent, node):
            if not node:
                if parent.val > val:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                return
            
            if node.val > val:
                insert(node, node.left)
            elif node.val < val:
                insert(node, node.right)
        
        if not root:
            return TreeNode(val)
        
        insert(root, root)
            
        return root
