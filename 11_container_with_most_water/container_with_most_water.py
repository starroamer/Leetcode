from typing import List

class Solution:
    """
    https://leetcode.cn/problems/container-with-most-water
    """
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        max_area = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area

if __name__ == "__main__":
    solution = Solution()
    nums = [1,8,6,2,5,4,8,3,7]
    res = solution.maxArea(nums)
    print(res)
