class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        left = 0
        right = n - 1
        insert_pos = -1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
                insert_pos = left
            else:
                right = middle - 1
                insert_pos = middle

        return insert_pos

if __name__ == "__main__":
    s = Solution()
    input = [1, 3, 5, 6]
    print(s.searchInsert(input, 0))
