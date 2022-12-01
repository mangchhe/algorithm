class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        traverse(res, candidates, new ArrayList<>(), 0, 0, target);
        return res;
    }
    
    private void traverse(List<List<Integer>> res, int[] candidates, ArrayList<Integer> list, int sum, int idx, int target) {
        if (sum == target) {
            res.add((List<Integer>) list.clone());
        }
        if (sum > target) {
            return;
        }
        
        for (int i = idx; i < candidates.length; i++) {
            list.add(candidates[i]);
            traverse(res, candidates, list, sum + candidates[i], i, target);
            list.remove(list.size() - 1);
        }
    }
}
