class Solution(object):
    """
    https://leetcode-cn.com/problems/integer-break/
    """
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 假设拆分为m个数字，拆分结果为k[0],k[1], ..., k[m-1]
        # k[m-1]大于等于4时，k[m-1]可继续拆分来获得更大的乘积，因此只需考虑k[m-1]=1,2,3的情形
        # k[m-1]=1时，必然取不到最大值，否则将k[m-2]与k[m-1]合并，即可获得更大乘积
        # 因此dp[i] = max(2*dp[i-2], 3*dp[i-3])
        if n < 4:
            return n - 1

        dp = [0, 1, 2, 3]
        for i in range(4, n + 1):
            max_score = max(2 * dp[i - 2], 3 * dp[i - 3])
            dp.append(max_score)

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(9))
