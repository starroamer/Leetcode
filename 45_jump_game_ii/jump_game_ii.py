class Solution:
    from typing import List
    """
    https://leetcode.cn/problems/jump-game-ii
    """
    def canJump(self, nums: List[int]) -> int:
        size = len(nums)
        end = 0  # 当前起跳点出发，一次跳跃能到达的最远位置
        max_pos = 0  # 当前起跳点出发，两次跳跃能到达的最远位置
        step = 0  # 跳跃次数
        for i in range(size - 1):
            max_pos = max(max_pos, i + nums[i])

            # 从上一个出发点start遍历到end，表示从start出发能到达的每一个位置，都计算过对应的max_pos了
            # 此时必然需要一次跳跃，增加step计数
            # 此次跳跃能到达的最远位置即为max_pos
            if i == end:
                end = max_pos
                step += 1
            print(i, nums[i], max_pos, end, step)

        return step


if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,1,2,4,2,3]
    print(solution.canJump(nums))
