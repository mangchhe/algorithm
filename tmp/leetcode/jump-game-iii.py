# https://leetcode.com/problems/jump-game-iii/

class Solution(object):
    def canReach(self, arr, start):
        if start >= len(arr) or start < 0 or arr[start] == -1:
            return False
        if arr[start] == 0:
            return True
        else:
            jmps = arr[start]
            arr[start] = -1
            return self.canReach(arr, start + jmps) | self.canReach(arr, start - jmps)
