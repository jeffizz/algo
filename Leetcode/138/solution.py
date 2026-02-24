#!/usr/bin/env python3

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        copy = curr = Node(0)
        while head:
            d[head] = Node(head.val) if head not in d else d[head]
            if head.random:
                if head.random not in d:
                    d[head].random = Node(head.random.val)
                    d[head.random] = d[head].random
                else:
                    d[head].random = d[head.random]
            curr.next = d[head]
            curr = curr.next
            head = head.next
        return copy.next if copy.next else None



