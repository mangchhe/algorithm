class Solution(object):
    def longestOnes(self, nums, k):
        zeros = [-1]
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        zeros.append(len(nums))
        if len(zeros) - k - 2 <= 0:
            return len(nums)
        
        for i in range(k + 1, len(zeros)):
            ans = max(ans, zeros[i] - zeros[i - k - 1] - 1)
            
        return ans
