class Solution(object):
    """
    https://leetcode-cn.com/problems/word-break/
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        n = len(s)
        assert n > 0
        dp = [False] * (n + 1)
        dp[0] = True
        wordDictSet = set(wordDict)
        max_word_len = max([len(x) for x in wordDict])
        for i in range(1, n + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                if i - j > max_word_len:
                    continue
                if s[j:i] not in wordDictSet:
                    continue
                dp[i] = True
                break

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    str = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(s.wordBreak(str, wordDict))
