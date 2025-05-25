class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        longest = s[0]  

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    candidate = s[i:j+1]
                    if candidate == candidate[::-1] and len(candidate) > len(longest):
                        longest = candidate

        return longest