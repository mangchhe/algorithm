class Solution(object):
    def binary_search(self, l, r, nums, target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        pivot = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                pivot = max(pivot, mid)
                l = mid + 1
            else:
                r = mid - 1
                
        a = self.binary_search(0, pivot, nums, target)
        b = self.binary_search(pivot + 1, len(nums) - 1, nums, target)

        if a == -1 and b == -1:
            return -1
        elif a == -1:
            return b
        else:
            return a
