# sorted
class Solution(object):
    def singleNumber(self, nums):
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return nums[i]

# hash
class Solution(object):
    def singleNumber(self, nums):
        isExist = {}
        for n in nums:
            if isExist.get(n):
                del isExist[n]
            else:
                isExist[n] = 1
        
        return isExist.keys()[0]

# xor
class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        
        for n in nums:
            ans ^= n
            
        return ans
