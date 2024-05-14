import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/merge-two-binary-trees/
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root2:
            return root1
        if not root1:
            return root2

        root = TreeNode()
        root.val = root1.val + root2.val
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root

if __name__ == "__main__":
    s = Solution()
    vals1 = [1,3,2,5]
    vals2 = [2,1,3,"null",4,"null",7]
    root1 = BinaryTreeUitl.makeBinaryTree(vals1)
    root2 = BinaryTreeUitl.makeBinaryTree(vals2)
    root = s.mergeTrees(root1, root2)
    BinaryTreeUitl.printBinaryTree(root)