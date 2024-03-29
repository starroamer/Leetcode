class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/house-robber-ii
    """
    def rob(self, nums: List[int]) -> int:
        value1 = self.do_rob(nums[1:])                 # 不选择第一间房子
        value2 = self.do_rob(nums[2:-1]) + nums[0]     # 选择第一间房子

        return max(value1, value2)

    def do_rob(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        dp = [0 for x in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    nums = [200,3,140,20,10]
    print(s.rob(nums))
