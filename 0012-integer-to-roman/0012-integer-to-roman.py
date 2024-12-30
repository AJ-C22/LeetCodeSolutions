class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        sub = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

        keys = list(values.keys())
        keys = sorted(keys)
        term = []
        count = 10
        while num > 0:

            rem = num % count
            count *= 10
            num -= rem
            s = ''
            if rem in sub:
                term.append(sub[rem])
            else:
                while rem > 0:
                    if rem >= 1000:
                        found = 1000
                    else: 
                        for i in range(len(keys)):
                            if rem < keys[i]:
                                found = keys[i-1]
                                break
                    s = s + values[found]
                    
                    rem -= found
                term.append(s)

        result = ''
        l = len(term) - 1  
        while l >= 0:
            result += term[l]  
            l -= 1  
        print(result)
        return result  
        