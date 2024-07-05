class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/jump-game/description
    """
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        size = len(nums)
        for i in range(size):
            # max_pos表示使用前i-1个元素能到达的最远处
            if max_pos >= i:
                # 位置i能到达, 判断经过与不经过第i个元素, 哪种情况走得更远, 并更新max_pos
                # 如果max_pos超过最后一个元素位置, 返回True
                max_pos = max(max_pos, i + nums[i])
                if max_pos >= size - 1:
                    return True
            else:
                # 位置i以及其后的位置都无法到达了，返回False
                return False

        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,1,0,4]
    print(solution.canJump(nums))
