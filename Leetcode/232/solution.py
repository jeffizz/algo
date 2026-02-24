#!/usr/bin/env python3

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) == 0 and len(self.stack2):
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        self.stack1.append(x)


    def pop(self) -> int:
        if len(self.stack2) == 0 and len(self.stack1):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    def peek(self) -> int:
        if len(self.stack2) == 0 and len(self.stack1):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


class MyQueue2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)


    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()


    def peek(self) -> int:
        if not self.stack2 and self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

