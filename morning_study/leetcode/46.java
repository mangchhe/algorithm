class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        traverse(res, new ArrayList<>(), new boolean[nums.length], nums);
        return res;
    }
    
    private void traverse(List<List<Integer>> res, List<Integer> tmp, boolean[] visited, int[] nums) {
        if (tmp.size() == nums.length) {
            res.add(new ArrayList<>(tmp));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) continue;
            
            visited[i] = true;
            tmp.add(nums[i]);
            traverse(res, tmp, visited, nums);
            tmp.remove(tmp.size() - 1);
            visited[i] = false;
        }
    }
}
