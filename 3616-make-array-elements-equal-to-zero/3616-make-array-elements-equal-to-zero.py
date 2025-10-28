class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        def traverse(arr, curr, direction):
            # Work in-place but isolated to this path
            while 0 <= curr < l:
                if arr[curr] == 0:
                    curr = curr + 1 if direction else curr - 1
                else:
                    arr[curr] -= 1
                    direction = not direction
                    curr = curr + 1 if direction else curr - 1
            return all(num == 0 for num in arr)

        count = 0
        for i in range(l):
            # can only start on a zero cell
            if nums[i] != 0:
                continue
            # simulate both directions using fresh copies
            if traverse(nums[:], i, True):
                count += 1
            if traverse(nums[:], i, False):
                count += 1

        return count
