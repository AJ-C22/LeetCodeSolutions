class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print(n)
        if n == 1:
            return True
        elif n % 3 != 0:
            return False
        elif n < 1:
            return False
        return self.isPowerOfThree(n/3)
        