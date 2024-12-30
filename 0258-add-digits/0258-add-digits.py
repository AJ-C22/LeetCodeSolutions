class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        mult = 10
        
        if num % 10 == num:
            return num 
        else:
            while num > 0:
                rem = num % mult
                num -= rem
                result += rem
                num /= 10
            
            return self.addDigits(result)

