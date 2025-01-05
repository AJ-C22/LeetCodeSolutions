class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a','e','i','o','u'}
        prefix_storing = [0] * len(words)
        
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_storing[i] = 1

        prefix_sum = [0] * (len(words) + 1)
        for i in range(len(prefix_storing)):
            prefix_sum[i + 1] = prefix_sum[i] + prefix_storing[i]

        result = []
        q = len(queries)

        print(prefix_storing)
        print(prefix_sum)
        for interval in queries:
            l, r = interval
            count = prefix_sum[r + 1] - prefix_sum[l]
            result.append(count)

        return result

        