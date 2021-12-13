class Solution(object):
    def maxPower(self, s):
        ans = 1
        cnt = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cnt += 1
                ans = max(ans, cnt)                
            else:
                cnt = 1
                
        return ans
