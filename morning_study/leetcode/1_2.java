class Solution {
    public int[] twoSum (int[] nums, int target) {
        Map<Integer, Integer> cache = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (cache.containsKey(nums[i])) {
                return new int[] {i, cache.get(nums[i])};
            }
            cache.put(target - nums[i], i);
        }
        
        return new int[2];
    }
}
