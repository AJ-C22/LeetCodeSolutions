class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        cloned = list(nums)
        for i in range(len(nums)):
            value = 0
            while True:
                rem = nums[i] % 10
                value += rem
                nums[i] -= rem
                if nums[i] == 0:
                    break
                else:
                    nums[i] /= 10
            if value in d:
                d[value].append(i)
            else:
                d[value] = [i]

        m = 0
        for key in d:
            if len(d[key]) > 1:
                vals = []
                for ind in d[key]:
                    vals.append(cloned[ind])
                vals.sort(reverse=True)  
                s = vals[0] + vals[1]
                if s > m:
                    m = s
        print(d)
        if m == 0:
            return -1
        return m          
        