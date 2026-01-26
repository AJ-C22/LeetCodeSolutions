class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result = []
        m = float('inf')
        arr.sort()
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) < m:
                m = abs(arr[i] - arr[i-1])
        
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) == m:
                result.append([arr[i-1],arr[i]])

        return result

        