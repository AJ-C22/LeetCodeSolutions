class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ['a','e','i','o','u','A','E','I','O','U']
        vowels = set(v)
        final = ''
        result = []
        for i in range(len(s)):
            result.append(s[i])

        i = 0
        j = len(s) - 1
 
        while i < j:
            print(i)
            print(j)
            print()
            if result[i] not in vowels:
                
                i += 1
            if result[j] not in vowels: 
                
                j -= 1
            if result[i] in vowels and result[j] in vowels:
                
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
                i += 1
                j -= 1

        for char in result:
            final += char
            
        return final
            
