import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/partition-list-lcci/
    """
    from typing import List, Optional
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找到链表中点
        if head is None or head.next is None:
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 翻转后半部分
        second_half_head = self.reverseList(slow.next)

        # 比较前半部分和翻转后的后半部分是否相等
        p1 = second_half_head
        p2 = head
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        lead = head
        end = None
        while lead:
            new_lead = lead.next
            lead.next = end
            end = lead
            lead = new_lead

        return end
        
if __name__   == "__main__":
    s = Solution()
    val = [1, 2, 2, 1]
    head = LinkedListUitl.makeLinkedList(val)
    print(LinkedListUitl.printLinkedList(head))
    print(s.isPalindrome(head))