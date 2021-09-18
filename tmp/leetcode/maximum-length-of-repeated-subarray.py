# https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/

class Solution(object):
    def findLength(self, nums1, nums2):
        num1Len = len(nums1)
        num2Len = len(nums2)
        res = 0
        tmp = [[0] * (num2Len + 1) for _ in range(num1Len + 1)]

        for i in range(1, num1Len + 1):
            for j in range(1, num2Len + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    res = max(tmp[i - 1][j - 1] + 1, res)
                    tmp[i][j] = tmp[i - 1][j - 1] + 1
                    
        return res