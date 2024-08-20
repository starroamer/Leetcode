import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/populating-next-right-pointers-in-each-node
    """
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        queue = []
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


if __name__ == "__main__":
    s = Solution()
    vals = [1,2,3,4,5,6,7]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    s.connect(root)