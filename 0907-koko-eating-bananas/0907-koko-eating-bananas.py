class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def checkBananas(k, piles, h):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k   
                if hours > h:                  
                    return False
            return True

        high = max(piles)
        low = 1
        lastTrue = high 
        while low <= high:
            m = low + (high - low) // 2
            answer = checkBananas(m, piles, h)
            if answer:
                lastTrue = m
            print(m, answer)
            if answer:
                high = m - 1
            elif not answer:
                low = m + 1

        return lastTrue


        
        