from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math

from collections import deque




class MaxQueue:

    def __init__(self):
        self.maxqueue = deque()
        self.size = 0
        self.maxvalue = None

    def max_value(self) -> int:
        return self.maxvalue or -1

    def push_back(self, value: int) -> None:
        if not self.maxvalue:
            self.maxvalue = value
        else:
            self.maxvalue = max(self.maxvalue, value)
        self.maxqueue.append(value)
        self.size += 1

    def pop_front(self) -> int:
        if self.size == 0: return -1
        tmp=self.maxqueue.popleft()
        right=self.size-1
        self.size=0
        self.maxvalue=None
        while right:
            self.push_back(self.maxqueue.popleft())
            right-=1

        return tmp



import queue
class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans



k=MaxQueue()
k.push_back(1)
k.push_back(2)
print(k.max_value())
print(k.pop_front())
print(k.max_value())
