class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        i = 0
        k = l - 1
        m = 0
        while i != k:
            print(m)
            print(k)
            print(i)
            area = (k - i) * min(height[i], height[k])
            if area > m:
                m = area
            if height[i] <= height[k]:
                i += 1
            elif height[i] > height[k]:
                k -= 1
        
        return m


# 1 4 6 5 2 10 9 4 11
# 0 1 2 3 4 5  6 7 8 