class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        j = len(height) - 1
        curr = 0
        i = 0
        while i < j:
            wid = min(height[i], height[j])
            length = j - i
            area = wid * length
            if wid == height[i]:
                i += 1
            else:
                j -= 1
            if area > curr:
                curr = area

        return curr
            

        
        