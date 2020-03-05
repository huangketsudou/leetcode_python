from typing import List
from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        self.size = 0
        self.substack = deque()
        self.top = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.size == 0:
            self.top = x
        self.stack.append(x)
        self.size += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #------------------------------
        #将s1中的元素全部弹出到s2中，在弹出s2中的栈顶元素就可以了

        if self.empty():
            raise Exception('Empty queue!')
        '''
        while self.size > 1:
            self.substack.append(self.stack.pop())
            self.size -= 1
        result = self.stack.pop()
        self.size=0
        while len(self.substack):
            self.push(self.substack.pop())
        '''
        while len(self.stack):
            self.substack.append(self.stack.pop())
        result=self.substack.pop()
        self.size=0
        while len(self.substack):
            self.push(self.substack.pop())

        return result


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            raise Exception('Empty queue!')
        return self.top

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0


k = MyQueue()
k.push(1)
k.push(2)
k.push(3)

print(k.pop())
print(k.peek())
# print(k.stack)
print(k.pop())
print(k.peek())
print(k.pop())
