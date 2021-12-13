class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
                
        return ans
