#!/usr/bin/env python3
# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        rhead = rcurr = ListNode()
        curr = head
        lhead, lcurr = ListNode(), head
        while curr:
            if curr.val < x:
                if not lhead.next:
                    lhead.next = curr
                lcurr = curr
            else:
                if lcurr is curr:
                    lcurr = curr.next
                else:
                    if lcurr: lcurr.next = curr.next
                rcurr.next = curr
                rcurr = rcurr.next
            if not curr.next:
                rcurr.next = None
                if lcurr: lcurr.next = rhead.next
                break;
            curr = curr.next
        return lhead.next if lhead.next else rhead.next

# head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
# result = Solution().partition(head, 3)
# head = ListNode(1, ListNode(4, ListNode(3, ListNode(0, ListNode(5, ListNode(2))))))
# result = Solution().partition(head, 2)
head = ListNode(1)
result = Solution().partition(head, 0)
while result:
    print(result.val)
    result = result.next

