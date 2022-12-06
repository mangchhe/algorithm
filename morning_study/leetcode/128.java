class Solution {
    public int longestConsecutive(int[] nums) {
        int res = 0;
        Set<Integer> cache = new HashSet<>();
        for (int num: nums) cache.add(num);

        for (int num: nums) {
            if (!cache.contains(num)) continue;

            int l = num, r = num, seq = 1;
            cache.remove(num);
            while (cache.contains(++r)) {
                seq++;
                cache.remove(r);
            }
            while (cache.contains(--l)) {
                seq++;
                cache.remove(l);
            }
            res = Math.max(res, seq);
        }

        return res;
    }
}
