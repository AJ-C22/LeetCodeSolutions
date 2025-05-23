class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # ()[{()()}]
        closed = [')', '}', ']']
        op = ['(', '{', '[']

        if len(s) <= 1:
            return False

        for char in s:
            if char in op:
                stack.append(char)
            if char in closed:
                if len(stack) == 0:
                    stack.append(char)
                elif char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False



        