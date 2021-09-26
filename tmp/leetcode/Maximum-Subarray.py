# https://leetcode.com/problems/maximum-subarray/

# 방법 1
# O(N^2)

def maxSubArray(nums):
    ans = -10 ** 4
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            ans = max(ans, sum(nums[i:j]))
    return ans

# 방법 2
# O(N)

def maxSubArray(nums):
    total, ans = 0, -10 ** 4
    for i in range(len(nums)):
        total += nums[i]
        if total <= nums[i]:
            total = nums[i]
        ans = max(total, ans)
    return ans
