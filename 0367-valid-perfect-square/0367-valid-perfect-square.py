class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num < 1:
            return False
    
        low, high = 1, num
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                low = mid + 1  # Search right half
            else:
                high = mid - 1  # Search left half
        
        return False 

        