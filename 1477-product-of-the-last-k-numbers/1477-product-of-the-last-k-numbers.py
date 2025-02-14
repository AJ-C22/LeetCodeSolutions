class ProductOfNumbers(object):

    def __init__(self):
        self.nums = []
        self.pref = [1]  # Initialize with 1 for multiplication identity

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.nums = []
            self.pref = [1]  # Reset everything if a zero is added
        else:
            self.nums.append(num)
            self.pref.append(self.pref[-1] * num)  # Maintain prefix product in normal order

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > len(self.nums):
            return 0  # If asking for more elements than available, return 0
        
        return self.pref[-1] // self.pref[-(k + 1)]  # Compute product of last `k` elements
