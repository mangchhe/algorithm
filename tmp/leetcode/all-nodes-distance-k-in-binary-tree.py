# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    parent = {}
    ans = []
    visited = [0] * 501
    def init(self, node):
        if node.left != None:
            self.parent[node.left.val] = node
            self.init(node.left)
        if node.right != None:
            self.parent[node.right.val] = node
            self.init(node.right)

    def dfs(self, node, k, cnt):
        self.visited[node.val] = 1
        if node == None or cnt > k:
            return
        if cnt == k:
            self.ans.append(node.val)
            return
        else:
            if self.parent[node.val] and not self.visited[self.parent[node.val].val]:
                self.dfs(self.parent[node.val], k, cnt + 1)
            if node.left and not self.visited[node.left.val]:
                self.dfs(node.left, k, cnt + 1)
            if node.right and not self.visited[node.right.val]:
                self.dfs(node.right, k, cnt + 1)

    def distanceK(self, root, target, k):
        self.parent = {}
        self.ans = []
        self.visited = [0] * 501
        self.parent[root.val] = None
        self.init(root)
        self.dfs(target, k, 0)

        return self.ans
