# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    from typing import List
    from typing import Optional
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: 
        paths = []
        path = []

        self.visit(root, path, paths)

        return paths
    
    def visit(self, node, path, paths):
        # 访问当前节点
        path.append(str(node.val))

        # 当前节点为叶子节点，将当前路径保存
        if node.left is None and node.right is None:
            path_str = "->".join(path)
            paths.append(path_str)

        # 访问左右子节点
        if node.left:
            self.visit(node.left, path, paths)
        if node.right:
            self.visit(node.right, path, paths)

        # 回溯至父节点，将当前节点从路径中删除
        path.pop()


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    paths = s.binaryTreePaths(root)
    for path in paths:
        print(path)
