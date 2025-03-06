class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        l = len(grid)
        total = []
        missing = 0
        double = 0
        d = {}
        for i in range(l):
            for num in grid[i]:
                total.append(num)

        total.sort()
        print(total)
        for i in range(1, l*l + 1):
            d[i] = 0
        for i in range(0,l*l):
            d[total[i]] += 1

        for key in d.keys():
            if d[key] == 2:
                double = key
            if d[key] == 0:
                missing = key
        print(d)
        return [double,missing]
