class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = []
        lower = s.lower()
        print(lower)
        for i in lower:
            if i.isalnum():
                n.append(i)
        
        print(n)

        l = len(n)
        for i in range(0,l):
            if n[i] == n[l - (i + 1)]:
                continue
            else:
                return False
        
        return True

        