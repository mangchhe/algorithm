class Solution {
    public int maxSubArray(int[] nums) {
        int l = 0, r = 0;
        int sum = Integer.MIN_VALUE;
        int res = Integer.MIN_VALUE;
        
        while (r < nums.length) {
            res = Math.max(res, sum);
            if (l == r) {
                sum = nums[l];
                r++;
                continue;
            }
            
            if (sum <= 0) {
                r = ++l;
                continue;
            }
            
            sum += nums[r++];
        }
        
        return Math.max(res, sum);
    }
}
