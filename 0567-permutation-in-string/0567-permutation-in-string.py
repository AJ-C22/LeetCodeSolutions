class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = {}
        w = {}
        l_s1 = len(s1)
        l_s2 = len(s2)
        for i in range(l_s1):
            d[s1[i]] = d.get(s1[i], 0) + 1
        
        for i in range(l_s2):
            w = {}
            if s2[i] not in d:
                
                continue
            
            else:
                window = s2[i:i + l_s1]
                
                if len(window) < l_s1:
                    return False
                
                for i in range(l_s1):
                    w[window[i]] = w.get(window[i], 0) + 1
                if w == d:
                    return True
        return False