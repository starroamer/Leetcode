import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/subtree-of-another-tree
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)

    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        先判断当前节点的子树是否与给定树相等，如相等则返回True，否则继续遍历左右子树
        """
        if root is None:
            return False
        return self.check(root, subRoot) or self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot)
    
    def check(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        if subRoot is None:
            return root is None

        if root.val != subRoot.val:
            return False

        return self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)

if __name__ == "__main__":
    s = Solution()
    vals = [3,4,5,1,2]
    sub_vals = [4,1,2]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    sub_root = BinaryTreeUitl.makeBinaryTree(sub_vals)
    print(s.isSubtree(root, sub_root))