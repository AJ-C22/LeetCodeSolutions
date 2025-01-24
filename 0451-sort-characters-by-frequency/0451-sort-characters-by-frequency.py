class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        print(d)
        val = d.values()
        val.sort()
        
        pairs = []
        for key in d:
            pairs.append([d[key], key])

        s = sorted(pairs, key=lambda x: x[0], reverse = True)
        result = ""
        for count, letter in s:
            for j in range(count):
                result += letter

        return result

