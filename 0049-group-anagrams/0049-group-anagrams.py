class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for i in strs:
            words_char = sorted(i)
            word = ''.join(words_char)
            if word in m:
                m[word].append(i)
            else:
                m[word] = [i]
        
        result = list(m.values())
        return result
        