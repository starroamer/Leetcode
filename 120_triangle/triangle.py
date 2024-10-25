class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/triangle/description
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            col = len(triangle[i])
            for j in range(col):
                if j == 0:
                    min_pre = dp[j]    
                elif j == col - 1:
                    min_pre = pre
                else:
                    min_pre = min(pre, dp[j])
                pre = dp[j]
                dp[j] = min_pre + triangle[i][j]

        return min(dp)
        
if __name__   == "__main__":
    s = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(s.minimumTotal(triangle))