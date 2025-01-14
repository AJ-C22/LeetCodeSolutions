class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        freqA = {}
        freqB = {}
        for i in range(len(A)):
            freqA[A[i]] = 0
            freqB[A[i]] = 0
        
        result = []
        for i in range(len(A)):
            freqA[A[i]] += 1
            freqB[B[i]] += 1
            count = 0
            
            for j in range(len(A)):
                if freqA[A[j]] == 1 and freqB[A[j]] == 1:
                    print(i)
                    count += 1
            result.append(count)

        return result
        