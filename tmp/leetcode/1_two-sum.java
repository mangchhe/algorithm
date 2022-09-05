class Solution {
    public int[] twoSum (int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> numMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            numMap.put(nums[i], numMap.getOrDefault(nums[i], 0) + 1);
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (target - nums[i] == nums[i] && numMap.get(nums[i]) < 2)
                continue;
            if (numMap.containsKey(target - nums[i])) {
                res[0] = i;
                res[1] = findNumIndex(nums, i, target - nums[i]);
                return res;
            }
        }
        return res;
    }
    
    private int findNumIndex(int[] nums, int startIndex, int target) {
        for (int i = startIndex + 1; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
