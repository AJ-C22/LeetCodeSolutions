class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = list(s)
        for char in s:
            stack.append(char)
            if char == "]":
                word = ""
                while True:
                    print(stack)
                    if stack:
                        prev = stack.pop()
                    else:
                        break
                    if prev == "[":
                        final_num = ""

                        while stack and stack[-1].isdigit():
                            final_num += stack.pop()

                        final_num = final_num[::-1]
                        num = int(final_num) if final_num else 1
                        break
                    else:
                        if prev == "]":
                            continue
                        word += prev
                decoded = word[::-1] * num
                for ch in decoded:
                    stack.append(ch)

        result = ""
        for char in stack:
            result += char
        return result
                