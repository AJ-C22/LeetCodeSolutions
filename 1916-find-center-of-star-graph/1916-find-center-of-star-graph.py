class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(edges)
        d = {}
        for parent, child in edges:
            if parent in d:
                d[parent] += 1
            else:
                d[parent] = 1
            if child in d:
                d[child] += 1
            else:
                d[child] = 1
        print(d)
        for key in d:
            if d[key] == n:
                return key
        
        