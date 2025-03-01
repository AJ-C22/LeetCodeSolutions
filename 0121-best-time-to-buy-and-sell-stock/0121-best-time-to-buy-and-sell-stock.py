class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = max(prices)
        diff = 0
        l = len(prices)
        for i in range(l):
            if prices[i] < m:
                m = prices[i]
            if prices[i] - m > diff:
                diff = prices[i] - m

        return diff
        

        