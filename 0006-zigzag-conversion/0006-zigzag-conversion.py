class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        d = {}
        for i in range(numRows):
            d[i + 1] = []

        l = len(s)
        inc = True
        j = 1
        for i in range(l):
            d[j].append(s[i])
            if j == numRows:
                inc = False
            elif j == 1:
                inc = True
            if inc:
                j += 1
            elif not inc:
                j -= 1

        result = ''
        for key in d.keys():
            for char in d[key]:
                result += char

        return result