#!/usr/bin/env python3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = ListNode()
        cur = head

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1 != None:
            cur.next = list1

        if list2 != None:
            cur.next = list2

        return head.next


list = []
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
result = Solution().mergeTwoLists(list1, list2)
while result != None:
    list.append(result.val)
    result = result.next
print(list)
