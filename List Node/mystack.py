from typing import List
from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.stack = deque()
        self.substack = deque()
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty(): raise Exception('Empty stack!')
        tmp = self.size
        self.size -= 1
        while tmp - 1 > 0:
            self.substack.append(self.stack.popleft())
            tmp -= 1
        target = self.stack.popleft()
        self.stack = self.substack
        self.substack = deque()
        return target

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty(): raise Exception('Empty stack!')
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        self.substack = deque()
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.substack.append(x)
        n = self.size
        while n > 0:
            self.substack.append(self.stack.popleft())
            n -= 1
        self.stack, self.substack = self.substack, self.stack
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            raise Exception('Empty stack!')
        self.size -= 1
        return self.stack.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


class MyStack3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        i = 0
        while i < self.size:
            self.stack.append(self.stack.popleft())
            i += 1
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            raise Exception('Empty stack!')
        self.size -= 1
        return self.stack.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            raise Exception('Empty stack!')
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


k = MyStack3()
k.push(1)
k.push(2)
print(k.pop())
print(k.pop())
print(k.pop())
