import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/diameter-of-binary-tree
    """
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPathLength(root)

        return self.max_diameter

    def maxPathLength(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_len = self.maxPathLength(root.left) + 1 if root.left else 0
        right_len = self.maxPathLength(root.right) + 1 if root.right else 0
        diameter = left_len + right_len
        self.max_diameter = max(diameter, self.max_diameter)
        return max(left_len, right_len)


if __name__ == "__main__":
    s = Solution()
    vals = [1,2,3,4,5]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    print(s.diameterOfBinaryTree(root))