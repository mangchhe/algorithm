# 이전 소스
class Solution(object):
    def countHomogenous(self, s):
        beforeS = s[0]
        cnt = 1
        ans = 0
        for i in range(1, len(s)):
            if beforeS == s[i]:
                cnt += 1
            else:
                ans += (1 + cnt) * cnt // 2
                beforeS = s[i]
                cnt = 1
        if len(s) == 1 or cnt == 1 and s[-1] != s[-2]:
            ans += 1
        elif cnt > 1:
            ans += (1 + cnt) * cnt // 2
            
        return ans % (10 ** 9 + 7)

# 개선 소스
class Solution(object):
    def countHomogenous(self, s):
        ans = 1
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        
        return ans % (10**9 + 7)
