class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = {}
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        
        values = list(m.values())
        values.sort(reverse=True)
        
        keys = []

        for i in range(0,k):
            for key, val in m.items():
                if val == values[i]:
                    keys.append(key)
                    del m[key]

        
        return keys
        

        