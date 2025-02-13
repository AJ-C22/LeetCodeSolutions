class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        operations = 0
        
        for i in range(len(nums)):
            if nums[i] >= k:
                count += 1

        heapq.heapify(nums)

        while count != len(nums):
            operations += 1
            
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            if x >= k:
                count -= 1
            if y >= k:
                count -= 1

            new = min(x, y) * 2 + max(x, y)
            if new >= k:
                count += 1
            heapq.heappush(nums, new)

        return operations

        