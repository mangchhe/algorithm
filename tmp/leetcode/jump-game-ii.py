# https://leetcode.com/problems/jump-game-ii/

def jump(nums):
        dp = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and dp[i + j] == 0:
                    dp[i + j] = dp[i] + 1

        return dp[len(nums) - 1]
