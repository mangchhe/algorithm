# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution(object):
    def traverse(self, node, visited):
        if not node:
            return
        if node.left:
            self.traverse(node.left, visited)
        visited.append(node.val)
        if node.right:
            self.traverse(node.right, visited)
        
    def inorderTraversal(self, root):
        ans = []
        self.traverse(root, ans)
        return ans

# Solution 2
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
