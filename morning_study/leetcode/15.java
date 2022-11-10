class Solution {
	public List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
		List<List<Integer>> result = new ArrayList<>();
		Map<List<Integer>, Boolean> resultCache = new HashMap<>();
		for(int i=0; i<nums.length-2; i++) {
			int target = nums[i];

			Map<Integer, Integer> cache = new HashMap<>();
			for(int j=i+1; j<nums.length; j++) {
				if (cache.containsKey(nums[j])) {
					List<Integer> element = List.of(nums[i], nums[j], cache.get(nums[j]));
					if (!resultCache.containsKey(element)) {
						result.add(element);
						resultCache.put(element, true);	
					}
				}
				cache.put(-(target + nums[j]), nums[j]);
			}
		}
		return result;
	}
}
