import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/kth-node-from-end-of-list-lcci
    """
    from typing import List, Optional
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        p1 = head
        for i in range(k - 1):
            p1 = p1.next
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2.val
        
        
if __name__   == "__main__":
    s = Solution()
    val = [1, 2, 3, 4, 5]
    head = LinkedListUitl.makeLinkedList(val)
    print(LinkedListUitl.printLinkedList(head))
    print(s.kthToLast(head, 2))