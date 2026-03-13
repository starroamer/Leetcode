import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
    """
    from typing import List, Optional
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        pA = headA
        pB = headB
        while pA or pB:
            if pA:
                pA = pA.next
                lenA += 1
            if pB:
                pB = pB.next
                lenB += 1

        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        if lenB > lenA:
            for i in range(lenB - lenA):
                pB = pB.next

        while pA and pB:
            if pA.val == pB.val:
                return pA
            pA = pA.next
            pB = pB.next

        return None

        
if __name__   == "__main__":
    s = Solution()
    val1 = [4,1,8,4,5]
    head1 = LinkedListUitl.makeLinkedList(val1)
    print(LinkedListUitl.printLinkedList(head1))
    val2 = [5,0,1,8,4,5]
    head2 = LinkedListUitl.makeLinkedList(val2)
    print(LinkedListUitl.printLinkedList(head2))
    node = s.getIntersectionNode(head1, head2)
    print(node.val)