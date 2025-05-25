class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1 

        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                return nums[i] - 1

        if nums[0] != 0:
            return 0
        else:
            return len(nums)
        