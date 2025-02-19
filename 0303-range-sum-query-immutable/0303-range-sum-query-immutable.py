class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list = nums
        l = len(self.list)
        self.pre  = [0] * l
        self.pre[0] = nums[0]
        for i in range(1,l):
            self.pre[i] = self.pre[i-1] + self.list[i] 


        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.pre[right]
        else:
            return self.pre[right] - self.pre[left - 1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)