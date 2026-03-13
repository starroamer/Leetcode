import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/partition-list-lcci/
    """
    from typing import List, Optional
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p = head
        small_head = ListNode(0)
        large_head = ListNode(0)
        small_p = small_head
        large_p = large_head
        while p:
            if p.val < x:
                small_p.next = ListNode(p.val)
                small_p = small_p.next
            else:
                large_p.next = ListNode(p.val)
                large_p = large_p.next
            p = p.next

        small_p.next = large_head.next

        return small_head.next
        
        
if __name__   == "__main__":
    s = Solution()
    val = [1,4,3,2,5,2]
    head = LinkedListUitl.makeLinkedList(val)
    print(LinkedListUitl.printLinkedList(head))
    head = s.partition(head, 3)
    print(LinkedListUitl.printLinkedList(head))