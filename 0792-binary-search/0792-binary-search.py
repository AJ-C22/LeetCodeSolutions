class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        j = l - 1
        m = 0
        i = 0
        while i <= j:
            print(i, j, m)
            m = i + (j - i) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                return m
        return -1



        