#!/usr/bin/env python3

from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        middle = head
        while head:
            c += 1
            head = head.next
        m = math.floor((c) / 2)
        while m > 0:
            middle = middle.next
            m -= 1
        return middle

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # @TODO
        # fast = slow = head
        # fast = fast.next.next
        # slow = slow.next
        pass

list = []
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
result = Solution().middleNode(head)
while result:
    list.append(result.val)
    result = result.next
print(list)
