# 이전 소스
class Solution(object):
    def construct2DArray(self, original, m, n):
        if m * n != len(original):
            return []
        
        ans = [[0] *  n for _ in range(m)]
        
        r, c = -1, 0
        for i in range(len(original)):
            if i % n == 0:
                r += 1
                c = 0
            ans[r][c] = original[i]
            c += 1
        
        return ans

# 개선 소스
class Solution(object):
    def construct2DArray(self, original, m, n):
        ans = []        
        if m * n != len(original):
            return []
        
        for i in range(m):
            ans.append(original[n * i : n * (i + 1)])
            
        return ans
