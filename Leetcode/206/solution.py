#!/usr/bin/env python3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        nhead = ListNode(head.val)
        while head:
            head = head.next
            if head:
                nhead = ListNode(head.val, nhead)
        return nhead


    # def reverseList(self, head: Optional[ListNode], prev = None) -> Optional[ListNode]:
    #     if head == None:
    #         return None
    #     if head.next:
    #         new_head = self.reverseList(head.next, head)
    #         head.next = prev
    #         return new_head
    #     else:
    #         head.next = prev
    #         return head


list = []
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = Solution().reverseList(head)
while result:
    list.append(result.val)
    result = result.next
print(list)
