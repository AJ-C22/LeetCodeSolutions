class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(nums, target, index):
            if not nums:  
                return index

            l = len(nums)
            mid = l // 2

            if nums[mid] == target:
                return index + mid  
            elif nums[mid] > target:
                return helper(nums[:mid], target, index)  
            else:  
                return helper(nums[mid+1:], target, index + mid + 1)  
    
        return helper(nums, target, 0) 