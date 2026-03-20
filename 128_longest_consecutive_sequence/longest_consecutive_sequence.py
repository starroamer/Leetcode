from typing import List

class Solution:
    """
    https://leetcode.cn/problems/longest-consecutive-sequence
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_len = 0
        for num in s:
            # 不是序列起点
            if num - 1 in s:
                continue

            # 当前数字是序列起点
            cur_len = 1
            while num + cur_len in s:
                cur_len += 1

            max_len = max(cur_len, max_len)
        return max_len

if __name__ == "__main__":
    s = Solution()
    nums = [100,4,200,1,3,2]
    print(s.longestConsecutive(nums))