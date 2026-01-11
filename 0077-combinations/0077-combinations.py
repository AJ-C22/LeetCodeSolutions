class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = deque([i for i in range(1,n+1)])

        result = []
        def backtracking(combo, start):
            if len(combo) == k:
                result.append(combo[:])
                return
            
            for i in range(start, len(nums)):
                if nums[i] in combo:
                    continue 
                combo.append(nums[i])
                
                backtracking(combo, i + 1)
                combo.pop()
            
            

            

        backtracking([], 0)
        return result
        