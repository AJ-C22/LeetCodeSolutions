class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        result = []
        for i in range(len(nums)):
            if freq[nums[i]] == 1:
                result.append(nums[i])

        return result
        
        