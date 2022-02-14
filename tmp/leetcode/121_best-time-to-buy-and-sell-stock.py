class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 0
        ans = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            ans = max(ans, prices[r] - prices[l])
            r += 1
            
        return ans
