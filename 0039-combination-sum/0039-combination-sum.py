class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(sm, lst, start):
            
            if sm == target:
                result.append(lst[:])
                return
            elif sm > target:
                return
            
            for i in range(start, len(candidates)):
                lst.append(candidates[i])
                sm += candidates[i]

                backtrack(sm, lst, i)

                lst.pop()
                sm -= candidates[i]
            
            
        backtrack(0, [], 0)
        return result
        