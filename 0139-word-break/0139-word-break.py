class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        memo = {}

        def helper(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    if helper(j):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return helper(0)



        