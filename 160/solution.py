#!/usr/bin/env python3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dA,dB = {},{}
        while headA and headB:
            dA[headA] = headA
            if headB in dA:
                return headB
            dB[headB] = headB
            if headA in dB:
                return headA
            headA = headA.next
            headB = headB.next
        while headA:
            if headA in dB:
                return headA
            headA = headA.next
        while headB:
            if headB in dA:
                return headB
            headB = headB.next

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # @TODO
        # a + (b - c) = b + (a - c)
        # https://leetcode.cn/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=selected-coding-interview
        pass

intersected = ListNode(8, ListNode(4, ListNode(5)))
headA = ListNode(4, ListNode(1, intersected))
headB = ListNode(5, ListNode(6, ListNode(1, intersected)))
result = Solution().getIntersectionNode(headA, headB)
while result:
    print(result.val)
    result = result.next
