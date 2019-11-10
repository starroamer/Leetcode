class Solution:
    """
    https://leetcode-cn.com/problems/3sum/
    """
    def threeSum(self, nums):
        result = []
        nums.sort()
        for k in range(len(nums)):
            # 最小值大于0，不可能得到解
            if nums[k] > 0:
                break
            # 最小值和前一个数重复，跳过以忽略重复解
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 双指针分别指向除nums[k]外的最小值和最大值
            i = k + 1
            j = len(nums) - 1
            while i < j:
                # 跳过双指针移动过程中遇到的重复值
                if i > k + 1 and nums[i] == nums[i - 1]:
                    print(k, i, j, "skip i: %d" % nums[i])
                    i += 1
                    continue
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    print(k, i, j, "skip j: %d" % nums[j])
                    j -= 1
                    continue
                # 计算三数之和，等于0则记录结果，小于0则向右移动左指针，大于0则向右移动右指针
                s = nums[k] + nums[i] + nums[j]
                if s == 0:
                    result.append((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif s < 0:
                    i += 1
                elif s > 0:
                    j -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [0, -4, -1, -4, -2, -3, 2]
    res = solution.threeSum(nums)
    print(res)
