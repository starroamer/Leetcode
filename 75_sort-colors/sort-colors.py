class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/sort-colors/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict
        if len(nums) == 1: return
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        
        start = 0
        for i in [0, 1, 2]:
            for j in range(start, start + dic[i]):
                nums[j] = i
            start += dic[i]

if __name__ == "__main__":
    solution = Solution()
    nums = [2,0,2,1,1,0]
    solution.sortColors(nums)
    print(nums)
