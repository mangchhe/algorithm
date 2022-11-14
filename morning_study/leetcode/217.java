class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> cache = new HashSet<>();
        
        for (int i=0; i<nums.length; i++) {
            if (cache.contains(nums[i])) {
                return true;
            }
            cache.add(nums[i]);
        }
        
        return false;
    }
}
