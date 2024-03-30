class Solution(object):
    """
    https://leetcode.cn/problems/delete-operation-for-two-strings
    """
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0 for i in range(len2)] for j in range(len1)]
        for i in range(len1):
            for j in range(len2):
                if i == 0:
                    dp[i][j] = j if word1[0] in word2[:j+1] else j + 2
                elif j == 0:
                    dp[i][j] = i if word2[0] in word1[:i+1] else i + 2
                else:
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 2)
                print(i, j, dp[i][j])

        return dp[len1-1][len2-1]


if __name__ == "__main__":
    s = Solution()
    word1 = "sea"
    word2 = "eat"
    print(s.minDistance(word1, word2))
