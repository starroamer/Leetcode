import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/sum-root-to-leaf-numbers
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.do_sum(root, 0)

    def do_sum(self, root, sum):
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        left_sum = self.do_sum(root.left, sum) if root.left else 0
        right_sum = self.do_sum(root.right, sum) if root.right else 0

        return left_sum + right_sum

if __name__ == "__main__":
    s = Solution()
    vals = [4,9,0,5,1]
    # vals = [1,2,3]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    print(s.sumNumbers(root))