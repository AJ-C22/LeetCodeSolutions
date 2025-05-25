class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        
        print(d)

        nums.sort()
        j = len(nums) - 1
        i = 0
        while i < j:
            s = nums[i] + nums[j]
            print(nums[i], nums[j])
            print(s)
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                if nums[i] == nums[j]:
                    return [d[nums[i]][0], d[nums[i]][1]]
                else:
                    return [d[nums[i]][0],d[nums[j]][0]]

        