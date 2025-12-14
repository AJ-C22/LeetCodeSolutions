class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        max_b = max(piles)

        def eating(speed):
            i = 0
            l = len(piles)
            count = 0
            while i < l:
                hours = (piles[i] + speed - 1) // speed
                count += hours
                if count > h:
                    return False
                i += 1

            return True
        i = 1
        j = max_b
        # 1 2 3 4 5 6 7 8 9 10
        curr = max_b
        while i <= j:
            m = (i + j) // 2
            result = eating(m)
            if not result:
                i = m + 1
            if result:
                if m < curr:
                    curr = m
                j = m - 1

        return curr
