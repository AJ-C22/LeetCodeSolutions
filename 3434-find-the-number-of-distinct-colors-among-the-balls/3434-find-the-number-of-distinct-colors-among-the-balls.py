class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        c = {}
        freq = {}
        l = len(queries)
        count = 0
        result = []
        for i in range(len(queries)):  
            ball = queries[i][0]
            colour = queries[i][1]

            if ball not in c:
                c[ball] = colour
                freq[colour] = freq.get(colour, 0) + 1
            else:
                old = c[ball]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]

                c[ball] = colour
                freq[colour] = freq.get(colour, 0) + 1

            result.append(len(freq))
                
        return result