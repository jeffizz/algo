#!/usr/bin/env python3
# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, j = head, head
        while i and j:
            i = i.next
            if j.next == None: return None
            else: j = j.next.next
            if i is j: break;
        while head and j:
            if head is j: break
            head = head.next
            j = j.next
        return head if j else None


