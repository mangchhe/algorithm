class Solution(object):
    def majorityElement(self, nums):
        numDic = {}
        moreN = len(nums) / 3
        ans = []
        for n in nums:
            numDic[n] = numDic.get(n, 0) + 1
            
        for n in numDic:
            if numDic[n] > moreN:
                ans.append(n)
                
        return ans
