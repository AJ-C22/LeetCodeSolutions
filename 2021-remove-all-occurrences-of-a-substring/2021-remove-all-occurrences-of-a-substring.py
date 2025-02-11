class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """

        if part not in s: 
            return s
        
        
        s = s.replace(part, "", 1)  
        
        
        return self.removeOccurrences(s, part)
