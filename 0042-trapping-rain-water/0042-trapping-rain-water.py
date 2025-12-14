class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
             #
        #.   # 
        #. # #
        ## ###
        ## ###
        left_max = [0]
        right_max = [0]
        r_max = 0
        l_max = 0
        for i in range(1,len(height)):
            if height[i-1] > l_max:
                l_max = height[i-1]
            left_max.append(l_max)

        j = len(height) - 2
        while j >= 0:
            if height[j+1] > r_max:
                r_max = height[j+1]
            right_max.append(r_max)
            j -= 1

        right_max.reverse()
        print(left_max)
        print(right_max)

        total = 0
        for i in range(len(height)):
            rain = min(left_max[i], right_max[i]) - height[i]
            print(rain)
            if rain > 0:
                total += rain

        return total




        