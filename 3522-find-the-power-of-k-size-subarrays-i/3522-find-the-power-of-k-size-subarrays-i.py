class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)
        result = []
        for i in range(l - k + 1):

            temp = nums[i: i + k]
            print(temp)

            status = True
            for i in range(len(temp) - 1):
                if temp[i] != temp[i+1] - 1:
                    status = False

            if status == False:
                result.append(-1)
            else:
                m = max(temp)
                result.append(m)

        return result

