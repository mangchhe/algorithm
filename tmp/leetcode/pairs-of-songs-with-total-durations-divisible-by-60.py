class Solution(object):
    def numPairsDivisibleBy60(self, time):
        res = 0
        remainders = {}
        for t in time:
            remainder = t % 60
            res += remainders.get((60 - remainder) % 60, 0)
            remainders[remainder] = remainders.get(remainder, 0) + 1
        return res
