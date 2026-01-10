class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        def backtracking(path, visited):
            if len(path) == len(nums):
                results.append(path[:])
                return
                
            
            for i in range(len(nums)):
                
                if i in visited:
                    continue
                path.append(nums[i])
                visited.add(i)

                print(path)
                backtracking(path, visited)
                path.pop()
                visited.remove(i)

        backtracking([],set())
        return results
            
