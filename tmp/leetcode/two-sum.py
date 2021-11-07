class Solution(object):
    def twoSum(self, nums, target):
        numDic = {}
        for i in range(len(nums)):
            if numDic.get(target - nums[i]) is None:
                numDic[nums[i]] = i
            else:
                return [i, numDic[target - nums[i]]]
