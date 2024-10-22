class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        larg = max(nums)
        small = min(nums)
        gcd = 0
        for i in range(1, small + 1):
            if small % i == 0 and larg % i == 0:
                gcd = i

        return gcd




        