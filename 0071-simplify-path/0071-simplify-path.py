class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        while "//" in path:
            path = path.replace("//", "/")

        l = len(path)
        print(path)
        sub = ''
        for i in range(1,l):
            print(sub)
            if path[i] == '/':
                if sub == ".." and stack:
                    stack.pop()
                    sub = ''
                elif sub == ".":
                    sub = ''
                    continue
                elif sub == ".." and not stack:
                    sub = ''
                    continue
                else:
                    stack.append(sub)
                sub = ''
                
            elif i == l - 1:
                sub += path[i]
                if sub == ".":
                    continue
                elif sub == ".." and stack:
                    stack.pop()
                elif sub == "..":
                    continue
                else: 
                    stack.append(sub)
            else:
                sub += path[i]

        
        result = ""
        if not stack:
            return "/"
        for s in stack:
            result += "/"
            result += s

        return result