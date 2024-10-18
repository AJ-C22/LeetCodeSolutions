class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        count = 0
        new = list(set(nums))
        new.sort()
        n = len(new)


        if n == 0:
            return 0

        elif n == 1:
            return 1

        for i in range(1, n):
            if new[i] == new[i - 1] + 1:
                count += 1
            else:
                l.append(count + 1)
                count = 0

            if i == n - 1:
                l.append(count + 1)
            

        return max(l)


# [0, 1, 1, 2]