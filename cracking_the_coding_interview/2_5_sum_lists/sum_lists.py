import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/partition-list-lcci/
    """
    from typing import List, Optional
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        result = ListNode(0)
        result_p = result
        addition = 0
        i = 1
        while p1 or p2:
            n1 = n2 = 0
            if p1:
                n1 = p1.val
                p1 = p1.next
            if p2:
                n2 = p2.val
                p2 = p2.next
            
            sum = n1 + n2 + addition
            if sum >= 10:
                sum -= 10
                addition = 1
            else:
                addition = 0
            result_p.next = ListNode(sum)
            result_p = result_p.next

        if addition > 0:
            result_p.next = ListNode(addition)

        return result.next
        
if __name__   == "__main__":
    s = Solution()
    val1 = [2,4,3]
    head1 = LinkedListUitl.makeLinkedList(val1)
    print(LinkedListUitl.printLinkedList(head1))
    val2 = [5,6,4]
    head2 = LinkedListUitl.makeLinkedList(val2)
    print(LinkedListUitl.printLinkedList(head2))
    print(LinkedListUitl.printLinkedList(s.addTwoNumbers(head1, head2)))