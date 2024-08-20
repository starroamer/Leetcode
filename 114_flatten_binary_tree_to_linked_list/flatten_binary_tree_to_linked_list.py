import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
from common.linked_list import LinkedListUitl
class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.do_flatten(root)

    # 返回root展开成链表后的尾节点
    def do_flatten(self, root):
        if root.left is None and root.right is None:
            return root
        
        # 左子树展开后的链表尾节点
        flatten_left_end = self.do_flatten(root.left) if root.left else None
        # 右子树展开后的链表尾节点
        flatten_right_end = self.do_flatten(root.right) if root.right else None

        # 展开操作
        if root.left:
            flatten_left_end.right = root.right
            root.right = root.left
            root.left = None

        return flatten_right_end if flatten_right_end else flatten_left_end


if __name__ == "__main__":
    s = Solution()
    vals = [1,2,5,3,4,'null',6]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    s.flatten(root)