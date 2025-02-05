class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        st1 = []
        st2 = []
        inds = []
        for i in range(len(s1)):
            st1.append(s1[i])
            st2.append(s2[i])
            if s1[i] == s2[i]:
                continue
            else:
                inds.append(i)
        
        if len(inds) == 0:
            return True
        elif len(inds) == 2:
            temp = st1[inds[0]] 
            st1[inds[0]] = st1[inds[1]] 
            st1[inds[1]] = temp
            print(inds)
            print(st1)
            print(st2)
            if st1 == st2:
                return True
            else: 
                return False
        else:
            return False

        

            
        