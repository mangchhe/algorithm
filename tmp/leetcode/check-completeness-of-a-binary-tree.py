# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def isCompleteTree(self, root):
        q = deque([(root, 1)])
        orders = []
        
        while q:
            node, order = q.popleft()
            orders.append(order)
            
            if node.left:
                q.append((node.left, order * 2))
            if node.right:
                q.append((node.right, order * 2 + 1))
            
        return orders[-1] == len(orders)
