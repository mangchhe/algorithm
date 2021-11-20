class Solution(object):
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 2
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == nums[mid^1]:
                l = mid + 1
            else:
                r = mid - 1
            
        return nums[l]
