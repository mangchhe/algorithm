# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution(object):
    
    def leftTraverse(self, node, visited):
        if not node:
            return [None]
        return [node.val] + self.leftTraverse(node.left, visited) + self.leftTraverse(node.right, visited)
    def rightTraverse(self, node, visited):
        if not node:
            return [None]
        return [node.val] + self.rightTraverse(node.right, visited) + self.rightTraverse(node.left, visited)
    
    def isSymmetric(self, root):
        if self.leftTraverse(root.left, []) == self.rightTraverse(root.right, []):
            return 1
        else:
            return 0

# Solution 2
class Solution(object):
    
    def traverse(self, leftNode, rightNode):
        if not leftNode and not rightNode:
            return 1
        if not leftNode or not rightNode:
            return 0
        if leftNode.val != rightNode.val:
            return 0
        
        return self.traverse(leftNode.left, rightNode.right) and self.traverse(leftNode.right, rightNode.left)
    
    def isSymmetric(self, root):
        return self.traverse(root.left, root.right)
