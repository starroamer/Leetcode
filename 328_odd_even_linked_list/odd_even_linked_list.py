import sys
sys.path.append("..")
from common.linked_list import ListNode, LinkedListUitl
class Solution(object):
    """
    https://leetcode.cn/problems/odd-even-linked-list
    """
    from typing import Optional
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        构造奇数和偶数链表，然后将其相连
        """
        if not head or not head.next:
            return head
        even_head = head.next
        odd_p = even_p = None
        p = head
        is_odd = True
        while p:
            if is_odd:
                if odd_p:
                    odd_p.next = p
                odd_p = p
            else:
                if even_p:
                    even_p.next = p
                even_p = p

            is_odd = not is_odd
            p = p.next
        
        odd_p.next = even_head
        even_p.next = None
        
        return head

if __name__ == "__main__":
    s = Solution()
    values = [2,1,3,5,6,4,7]
    head = LinkedListUitl.makeLinkedList(values)
    odd_even_head = s.oddEvenList(head)
    print(LinkedListUitl.printLinkedList(odd_even_head))
