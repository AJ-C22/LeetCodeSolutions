class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        result = 0
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                value1 = stack.pop()
                value2 = stack.pop()
                if i == '+':
                    result = int(value1) + int(value2)
                elif i == '-':
                    result = int(value2) - int(value1)
                elif i == '*':
                    result = int(value2) * int(value1)
                elif i == '/':
                    if int(value2) * int(value1) > 0:
                        result = int(int(value2) / int(value1)) 
                    else:
                        result = -int(-int(value2) // int(value1))
                
                stack.append(result)

        return int(stack[0])
        