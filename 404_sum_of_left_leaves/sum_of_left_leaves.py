import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/sum-of-left-leaves
    """
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.addLeftLeaves(root.left, True) + self.addLeftLeaves(root.right, False)
    
    def addLeftLeaves(self, root: Optional[TreeNode], is_left_child):
        if not root:
            return 0 
        if not root.left and not root.right:
            return root.val if is_left_child else 0

        return self.addLeftLeaves(root.left, True) + self.addLeftLeaves(root.right, False)

if __name__ == "__main__":
    s = Solution()
    vals = [3, 9, 20, 'null', 'null', 15, 7]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    print(s.sumOfLeftLeaves(root))