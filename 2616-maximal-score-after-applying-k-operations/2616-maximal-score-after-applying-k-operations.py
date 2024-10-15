class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        count = 0
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            count += largest
            
            new_value = int(math.ceil(largest / 3.0))
            heapq.heappush(max_heap, -new_value)
    
        return count

        