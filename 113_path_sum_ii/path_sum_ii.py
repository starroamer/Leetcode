import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/path-sum-ii/
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        path = []
        self.visit(root, path, targetSum, results)
        return results

    def visit(self, root, path, targetSum, result):
        """
        root: 访问的节点
        path: 访问到该节点之前经过的路径
        targetSum: 访问到该节点时还剩余的targetSum
        result: 记录所有结果的列表
        """
        if root is None:
            return
        path.append(root.val) # 当前节点加入路径
        if root.left is None and root.right is None and root.val == targetSum:
            # 叶子节点，且路径总和满足要求
            # 将路径加入result
            # 注意使用[:]复制path，避免后续修改path影响result里的值
            result.append(path[:])
        else:
            # 深度遍历
            if root.left:
                self.visit(root.left, path, targetSum - root.val, result)
            if root.right:
                self.visit(root.right, path, targetSum - root.val, result)

        # 回溯，当前节点从路径中删除
        path.pop()

        

if __name__ == "__main__":
    s = Solution()
    vals = [5, 4, 8, 11, "null", 13, 4, 7, 2, "null", "null", 5, 1]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    targetSum = 22
    print(s.pathSum(root, targetSum))