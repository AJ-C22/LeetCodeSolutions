class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}  
        l = len(nums)
        total_pairs = (l * (l - 1)) // 2
        good_pairs = 0  

        for i in range(l):
            diff = nums[i] - i  
            if diff in d:
                good_pairs += d[diff]
                d[diff] += 1
            else:
                d[diff] = 1

        return total_pairs - good_pairs  
