# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a Node.
# class Node(object):
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution(object):

    nodes = []

    def dfs(self, node):

        if node == None:
            return
        self.nodes.append(node)
        if node.child:
            self.dfs(node.child)
        if node.next:
            self.dfs(node.next)

    def flatten(self, head):

        self.nodes = []

        if not head:
            return None

        self.dfs(head)

        head = self.nodes[0]
        head.child = None

        for i in range(1, len(self.nodes)):
            node = self.nodes[i]
            prev = self.nodes[i - 1]
            node.child = None
            node.prev = prev
            prev.next = node


        return head
