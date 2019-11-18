class Solution(object):
    """
    https://leetcode-cn.com/problems/next-permutation/
    """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = 0
        if n == 0:
            return

        # 找到进位点k
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = i
                break
        if k > 0:
            # 交换k-1位元素和k位后最小的大于nums[k - 1]的元素
            i = k
            while i < n - 1:
                if nums[i + 1] <= nums[k - 1]:
                    break
                i += 1
            nums[i], nums[k - 1] = nums[k - 1], nums[i]

        # 保持k位以后的元素倒序排序
        # for i in range(k, n - 1):
        #     if nums[i] >= nums[i + 1]:
        #         break
        #     nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # 将k位以后的元素逆序，构成字典序最小序
        i = k
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    s = Solution()
    nums = [9,8,1,6,4,3]
    s.nextPermutation(nums)
    print(nums)