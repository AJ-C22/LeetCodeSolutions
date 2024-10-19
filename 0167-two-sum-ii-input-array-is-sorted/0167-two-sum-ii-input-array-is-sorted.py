class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(numbers)
        k = l - 1
        i = 0
        while i < l:
            print(str(numbers[i]) + ':' +str(numbers[k]))
            if numbers[i] + numbers[k] > target:
                k -= 1
            elif numbers[i] + numbers[k] < target:
                i += 1
            else:
                return [i + 1, k + 1]
            

# [-2, -1, 0, 3, 5]
# target = 4







        