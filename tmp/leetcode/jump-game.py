# https://leetcode.com/problems/jump-game/

def canJump(nums):
    jmps = nums[0]
    idx = 0
    while idx < len(nums):
        jmps -= 1
        idx += 1
        if jmps == 0:
            break

        if idx < len(nums) and jmps < nums[idx]:
            jmps = nums[idx]

    return True if idx == len(nums) or len(nums) == 1 else False


print(canJump([2, 0, 0]))
