class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        l = len(nums)
        count = 0
        less = []
        more = []
        equal = []
        c1 = 0
        c2 = 0
        c3 = 0
        result = []
        for i in range(l):
            if nums[i] < pivot:
                less.append(nums[i])
                c1 += 1
            elif nums[i] > pivot:
                more.append(nums[i])
                c3 += 1
            else:
                equal.append(pivot)
                c2 += 1

        for i in range(c1):
            result.append(less[i])
        for i in range(c2):
            result.append(equal[i])
        for i in range(c3):
            result.append(more[i])
        
        return result

                
    
        