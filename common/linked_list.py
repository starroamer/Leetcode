from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListUitl:
    @staticmethod
    def makeLinkedList(vals):
        val_num = len(vals)
        node = None
        next = None
        for i in range(val_num - 1, -1, -1):
            node = ListNode(vals[i], next)
            next = node

        return node

    @staticmethod
    def printLinkedList(head: Optional[ListNode]):
        node_list = []
        p = head
        while p:
            node_list.append(str(p.val))
            p = p.next

        s = "->".join(node_list)
        return s