# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    numDic = {}
    oddCnt = 0
    ans = 0

    def solve(self, node):
        if not self.numDic.get(node.val):
            self.numDic[node.val] = 1
            self.oddCnt += 1
        else:
            self.numDic[node.val] += 1
            self.oddCnt = self.oddCnt - 1 if self.numDic[node.val] % 2 == 0 else self.oddCnt + 1

        if not (node.left or node.right):
            if self.oddCnt < 2:
                self.ans += 1
        else:
            if node.left:
                self.solve(node.left)
            if node.right:
                self.solve(node.right)

        if self.numDic.get(node.val) % 2 == 0:
            self.numDic[node.val] -= 1
            self.oddCnt += 1
        else:
            self.oddCnt -= 1
            if self.numDic.get(node.val) == 1:
                del self.numDic[node.val]
            else:
                self.numDic[node.val] -= 1

    def pseudoPalindromicPaths (self, root):

        self.numDic = {}
        self.oddCnt = 0
        self.ans = 0

        self.solve(root)

        return self.ans
