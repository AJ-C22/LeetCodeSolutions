class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        l = len(nums)
        n = l/2
        for i in range(l):
            if nums[i] not in d:
                d[nums[i]] = 1
                if d[nums[i]] > n:
                    return nums[i]
            else:
                d[nums[i]] += 1
                if d[nums[i]] > n:
                    return nums[i]
        
        