# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    ans = []

    def solve(self, node):
        self.ans.append(node.val)
        if node.left:
            self.solve(node.left)
        if node.right:
            self.solve(node.right)

    def kthSmallest(self, root, k):
        self.ans = []
        self.solve(root)
        return sorted(self.ans)[k - 1]
