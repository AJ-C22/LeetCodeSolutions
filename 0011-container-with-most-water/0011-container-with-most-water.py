class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        j = l - 1
        i = 0
        area = 0
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            if w * h > area:
                area = w * h
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1

        return area
