class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/remove-duplicates-from-sorted-array
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        p = 1 # num[0:p+1]满足条件
        for i in range(p + 1, n):
            if nums[i] != nums[p] or nums[i] != nums[p - 1]:
                p += 1
                nums[p] = nums[i]
            print("i = ", i, "p = ", p, "nums=", nums)

        del nums[p + 1:]
        return p + 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    k = solution.removeDuplicates(nums)
    print(k)
    print(nums)
