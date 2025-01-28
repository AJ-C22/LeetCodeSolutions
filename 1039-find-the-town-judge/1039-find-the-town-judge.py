class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        
        t= {}
        for truster, trustee in trust:
            if trustee in t:
                t[trustee][1] += 1
            else:
                t[trustee] = [0,1]

            if truster in t:
                t[truster][0] += 1
            else:
                t[truster] = [1,0]

        unique = []
        for i in trust:
            if i[0] not in unique:
                unique.append(i[0])

        u = len(unique)
        if u < n - 1:
            return -1
            
        print(t)
        for key in t:
            if t[key][0] == 0 and t[key][1] == u:
                return key
        
        return -1

        