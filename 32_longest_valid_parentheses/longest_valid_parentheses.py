class Solution(object):
    """
    https://leetcode-cn.com/problems/longest-valid-parentheses/
    """
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        if str_len < 2:
            return 0
        dp = [0] * str_len
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == "(":
                continue
            if s[i - 1] == "(":
                # s = "...()"
                dp[i] = 2
                if i - 2 >= 0:
                    dp[i] += dp[i - 2]
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                # s = "...))"
                dp[i] = dp[i - 1] + 2
                if i - dp[i - 1] - 2 >= 0:
                    dp[i] += dp[i - dp[i - 1] - 2]

            max_len = max(max_len, dp[i])

        return max_len


if __name__ == "__main__":
    s = Solution()
    input = "(())())()(())))("
    max_len = s.longestValidParentheses(input)
    print(max_len)
