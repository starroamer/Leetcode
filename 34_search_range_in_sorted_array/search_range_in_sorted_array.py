class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        n = len(nums)
        start = -1
        end = -1
        left = 0
        right = n - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target and (middle == 0 or nums[middle - 1] < nums[middle]):
                start = middle
                break
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        if start == -1:
            return [-1, -1]

        left = start
        right = n - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target and (middle == n - 1 or nums[middle] < nums[middle + 1]):
                end = middle
                break
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return [start, end]


if __name__ == "__main__":
    s = Solution()
    input = []
    start, end = s.searchRange(input, 10)
    print(start, end)
