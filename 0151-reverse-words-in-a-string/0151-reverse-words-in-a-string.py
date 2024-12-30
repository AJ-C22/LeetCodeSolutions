class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        l = len(words)
        result = ''

        while l > 0:
            result += words[l-1] 
            if l != 1:
                result += ' '
            l -= 1
        print(words)
        return result
                

