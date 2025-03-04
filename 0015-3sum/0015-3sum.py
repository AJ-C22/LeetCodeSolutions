class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        results = set()

        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, l - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    results.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return [list(triplet) for triplet in results]
        