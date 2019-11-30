class Solution(object):
    """
    https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        warp = self.findwarp(nums)
        print(warp)

        if target >= nums[0]:
            left = 0
            right = warp
        else:
            left = warp + 1
            right = len(nums) - 1
        if warp == -1:
            left = 0
            right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    def findwarp(self, nums):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            middle = left + (right - left) // 2
            print(left, right, middle)
            if middle == n - 1:
                return -1
            if nums[middle] > nums[middle + 1]:
                return middle
            if nums[middle] >= nums[0]:
                left = middle + 1
            else:
                right = middle

        return -1


if __name__ == "__main__":
    s = Solution()
    input = [15,16]
    idx = s.search(input, 15)
    print(idx)