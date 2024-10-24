class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' and stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == ']' and stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif i == '}' and stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False
# (([)])
# (([]))[] 