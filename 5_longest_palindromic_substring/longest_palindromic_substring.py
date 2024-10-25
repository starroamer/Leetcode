class Solution:
    """
    https://leetcode.cn/problems/longest-palindromic-substring
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        max_len = 1
        result = s[0]
        for k in range(1, n):
            for i in range(n):
                j = i + k
                if j >= n:
                    continue
                if k == 1:
                    dp[i][j] = 2 if s[j] == s[i] else 0
                else:
                    if dp[i + 1][j - 1] > 0 and s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = 0
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    result = s[i:j + 1]

        return result

        
if __name__   == "__main__":
    s = Solution()
    input = "babad"
    print(s.longestPalindrome(input))