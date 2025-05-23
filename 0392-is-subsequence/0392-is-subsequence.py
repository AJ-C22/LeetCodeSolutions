class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0 
        if s == "":
            return True
        
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1
                
        return j == len(s)