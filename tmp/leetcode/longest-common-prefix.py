# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        idx = 1
        ans = ''
        while idx < len(strs[0]) + 1:
            s = strs[0][0:idx]
            for i in range(1, len(strs)):
                if s == strs[i][0:idx]:
                    pass
                else:
                    idx = len(s) + 1
                    break
            else:
                ans = strs[0][0:idx]
            idx += 1

        return ans
