# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    ans = []

    def preorder(self, node):
        if node is None:
            return
        self.ans.append(node)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def flatten(self, root):
        if root is None:
            return

        self.preorder(root)

        head = self.ans[0]

        for i in range(1, len(self.ans)):
            node = self.ans[i]
            prev = self.ans[i - 1]
            prev.left = None
            prev.right = node

        return head
