class Solution {
    public int[] twoSum (int[] nums, int target) {
        int[] originNums = Arrays.copyOfRange(nums, 0, nums.length);
        
        Arrays.sort(nums);
        
        int l = 0;
        int r = nums.length - 1;
        int[] ret = new int[2];
        
        while (l < r) {
            int sum = nums[l] + nums[r];
            
            if (sum == target) {
                ret[0] = findIndex(originNums, nums[l]);
                ret[1] = findIndexFromEnd(originNums, nums[r]);
                return ret;
            }
            if (sum > target) {
                r--;
            }
            if (sum < target) {
                l++;
            }
        }
        
        return new int[2];
    }
    
    private int findIndex(int[] originNums, int target) {
        for (int i = 0; i < originNums.length; i++) {
            if (originNums[i] == target) {
                return i;
            }
        }
        return -1;
    }
    
    private int findIndexFromEnd(int[] originNums, int target) {
        for (int i = originNums.length-1; i > -1; i--) {
            if (originNums[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
