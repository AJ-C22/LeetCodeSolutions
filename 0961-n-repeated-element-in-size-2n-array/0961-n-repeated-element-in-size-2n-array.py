class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        n = l / 2
        d = {}
        for i in range(l):
            if nums[i] not in d:
                d[nums[i]] = 0
            d[nums[i]] += 1
            if d[nums[i]] == n:
                return nums[i]

        