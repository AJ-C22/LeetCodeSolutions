class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = max(prices)
        prof = 0
        for num in prices:
            if num < low:
                low = num
            if num - low > prof:
                prof = num - low

        return prof
            

        