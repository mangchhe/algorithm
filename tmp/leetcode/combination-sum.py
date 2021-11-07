class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        def dfs(candis, target, idx):
            if target < 0:
                return
            elif target == 0:
                ans.append(candis[:])
            elif idx >= len(candidates):
                return
            else:
                candis.append(candidates[idx])
                dfs(candis, target - candidates[idx], idx)
                candis.pop()
                dfs(candis, target, idx + 1)
        
        dfs([], target, 0)
        
        return ans
