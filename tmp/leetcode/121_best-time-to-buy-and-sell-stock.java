class Solution {
    public int maxProfit(int[] prices) {
        int l=0, r=0;
        int res=0;
        
        while (r < prices.length) {
            if (l == r) {
                r++;
                continue;
            }
            
            if (prices[l] > prices[r]) {
                l = r++;
                continue;
            }
            
            res = Math.max(res, prices[r] - prices[l]);
            r++;
        }
        
        return res;
    }
}
