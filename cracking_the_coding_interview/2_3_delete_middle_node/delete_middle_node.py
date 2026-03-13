import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/delete-middle-node-lcci
    """
    from typing import List, Optional
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
        
if __name__   == "__main__":
    s = Solution()
    val = [4, 5, 1, 9]
    head = LinkedListUitl.makeLinkedList(val)
    print(LinkedListUitl.printLinkedList(head))
    s.deleteNode(head.next)
    print(LinkedListUitl.printLinkedList(head))