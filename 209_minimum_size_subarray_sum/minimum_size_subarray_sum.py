from typing import List

class Solution:
    """
    https://leetcode.cn/problems/minimum-size-subarray-sum
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        i = 0
        j = 0
        sum = nums[i]
        while i < n:
            print(sum, i, j)
            if sum >= target:
                min_len = min(min_len, j - i + 1)
                print("update min_len=", min_len)
                sum -= nums[i]
                i += 1
            elif j < n - 1:
                sum += nums[j + 1]
                j += 1
            else:
                break

        min_len = 0 if min_len == float('inf') else min_len
        return min_len


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,1,1,1,1,1]
    target = 11
    print(s.minSubArrayLen(target, nums))