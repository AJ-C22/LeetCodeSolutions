class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 0 1 0 3 12
        # 1 0 0 3 12
        # 1 3 0 0 12
        # 1 3 12 0 0

        # 1 3 0 4 0 0 6
        # 1 3 4 0 0 0 6
        j = 0
        l = len(nums)
        for i in range(l):
            if nums[j] == 0 and nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
            elif nums[j] == 0:
                continue
            else:
                j += 1



        