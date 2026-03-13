import sys
sys.path.append("../..")
from common.linked_list import ListNode, LinkedListUitl

class Solution:
    """
    https://leetcode.cn/problems/remove-duplicate-node-lcci/description/
    """
    from typing import List, Optional
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        vals = set()
        cur = head
        new_head = None
        new_cur = None
        while cur:
            if cur.val not in vals:
                if new_cur is None:
                    new_cur = ListNode(cur.val)
                    new_head = new_cur
                else:
                    new_cur.next = ListNode(cur.val)
                    new_cur = new_cur.next
                vals.add(cur.val)
            cur = cur.next

        return new_head
            
        
        
if __name__   == "__main__":
    s = Solution()
    val = [1, 1, 1, 1, 2]
    head = LinkedListUitl.makeLinkedList(val)
    print(LinkedListUitl.printLinkedList(head))
    head = s.removeDuplicateNodes(head)
    print(LinkedListUitl.printLinkedList(head))