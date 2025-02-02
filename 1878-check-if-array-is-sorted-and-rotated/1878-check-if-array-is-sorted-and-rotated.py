class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        if nums[0]<nums[-1]:
            count+=1
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                count+=1
        if count>1:
            return False
        return True