from typing import List

class Solution:
    """
    https://leetcode.cn/problems/non-decreasing-array/
    """
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True

        ret = True
        has_decrease = False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if has_decrease:
                    # 存在两处逆序，不满足
                    ret = False
                    break
                else:
                    increase_ok = nums[i + 2] >= nums[i] if i < n - 2 else True  # 增加nums[i + 1]可满足
                    decrease_ok = nums[i - 1] <= nums[i + 1] if i > 0 else True  # 减小nums[i]可满足
                    ret = increase_ok or decrease_ok

                has_decrease = True

        return ret



if __name__ == "__main__":
    nums = [4, 2, 3]
    s = Solution()
    print(s.checkPossibility(nums))
