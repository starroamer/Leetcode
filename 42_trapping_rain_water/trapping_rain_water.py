from typing import List

class Solution:
    """
    https://leetcode.cn/problems/trapping-rain-water
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [height[0]] * n           # 往左边看过去的最高点
        right_max = [height[n - 1]] * n      # 往右边看过去的最高点

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
            right_max[n - 1 - i] = max(height[n - 1 - i], right_max[n - i])

        area = 0
        for i in range(n):
            # 每个点可接雨水的量为左右最高点的最小值 - 该点本身的高度
            area += min(left_max[i], right_max[i]) - height[i]

        return area

if __name__ == "__main__":
    solution = Solution()
    height = [4,2,0,3,2,5]
    res = solution.trap(height)
    print(res)
