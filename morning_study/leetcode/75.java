class Solution {
    public void sortColors(int[] nums) {
        int[] colors = new int[3];
        
        for (int num: nums) colors[num]++;
        
        int color = 0, idx = 0;
        while (color < 3) {
            if (colors[color] != 0) {
                nums[idx] = color;
                colors[color]--;
                idx++;
            }
            if (colors[color] == 0) color++;
        }
    }
}
