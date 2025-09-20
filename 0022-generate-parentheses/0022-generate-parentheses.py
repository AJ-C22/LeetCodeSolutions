class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 0
        bracket = []
        def helper(count, brackets, open, closed, answer):
            if closed > open:
                return
            if open > n or closed > n:
                return 
            if count == n*2 and open == closed:
                answer.append(brackets)
                return 
            if open < n:
                helper(count + 1, brackets + "(", open + 1, closed, answer)
            if closed < n:
                helper(count + 1, brackets + ")", open, closed + 1, answer)
        answer = []
        helper(0,"",0,0,answer)
        return answer
        



        
        