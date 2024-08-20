import sys
sys.path.append("..")
from common.tree import TreeNode, BinaryTreeUitl
from common.linked_list import LinkedListUitl
class Solution:
    from typing import List, Optional
    """
    https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii
    """
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (root.left is None and root.right is None):
            return root
        
        # 从根节点开始
        head = root
        
        while head:
            
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            cur = head
            child_num = 0
            child_head = None
            child_cur = None
            while cur:
                cur_left_most_child = cur.left if cur.left else cur.right
                if child_head is None:
                    child_head = cur_left_most_child
                    child_cur = child_head

                child_next = cur_left_most_child
                # 连接两个节点之间的子节点
                if child_next and child_cur != child_next:
                    child_cur.next = child_next
                    child_cur = child_next

                # 连接节点的左右子节点
                if cur.left and cur.right:
                    cur.left.next = cur.right
                    child_cur = cur.right

                # 指针向后移动
                cur = cur.next
            
            LinkedListUitl.printLinkedList(child_head)
            # 去下一层的最左的节点
            head = child_head
        
        return root


if __name__ == "__main__":
    s = Solution()
    vals = [1,2,3,4,5,"null",6,7,"null","null","null","null",8]
    root = BinaryTreeUitl.makeBinaryTree(vals)
    s.connect(root)