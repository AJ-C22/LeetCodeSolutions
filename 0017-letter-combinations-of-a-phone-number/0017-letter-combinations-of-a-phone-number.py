class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h", "i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        nums = list(digits)
        l = len(nums)
        result = []
        def backtrack(combo,start):
            if len(combo) == l:
                s = ""
                for char in combo[:]:
                    s += char
                result.append(s)
                return
            
            for i in range(start,len(nums)):
                lst = d[nums[i]]
                for j in range(len(lst)):

                    combo.append(lst[j])
                    backtrack(combo,i + 1)
                    
                    combo.pop()
                    

        backtrack([],0)
        return result


        