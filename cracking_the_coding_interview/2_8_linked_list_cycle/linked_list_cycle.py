import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/linked-list-cycle-lcci/
    """
    from typing import List, Optional
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

        
if __name__   == "__main__":
    s = Solution()
    val = [3, 2, 0, -4]
    head = LinkedListUitl.makeLinkedList(val)
    print(LinkedListUitl.printLinkedList(head))
    print(s.detectCycle(head))