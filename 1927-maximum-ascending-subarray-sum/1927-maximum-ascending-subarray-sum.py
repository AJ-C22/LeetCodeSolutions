class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        l = len(nums)
        if l == 1:
            return nums[0]
            
        for i in range(l - 1):
            if nums[i] > nums[i + 1]:
                if nums[i] > count:
                    count = nums[i]
                    continue
    
            else:
                sub = 0
                for j in range(i,l-1):
                    print(nums[j])
                    sub += nums[j]
                    if j == l-2 and nums[j] < nums[j+1]:
                        print(nums[j+1])
                        sub += nums[j+1]
                        break
                    if nums[j] < nums[j+1]:
                        continue
                    else:
                        break
                if sub > count:
                    count = sub

        return count





        