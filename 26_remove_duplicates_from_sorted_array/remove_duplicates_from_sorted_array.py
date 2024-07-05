class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/remove-duplicates-from-sorted-array
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        for j in range(1, n):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i


if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = solution.removeDuplicates(nums)
    print(k)
    print(nums)
