class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1

        print(d)
        total = 0
        odd = 0
        for key, count in d.items():
            print(key, count)
            if count % 2 == 0:
                total += count
            else:
                total += count - 1
                odd = 1

        return total + odd
        