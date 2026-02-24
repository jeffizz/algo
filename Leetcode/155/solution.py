#!/usr/bin/env python3

class Node:
    def __init__(self, x: int, min: int):
            self.val = x
            self.min = min

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min = self.getMin() if self.stack else val
        if min > val:
            min = val
        self.stack.append(Node(val, min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
