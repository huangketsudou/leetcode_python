from typing import List
from collections import deque


'''
摊还分析给出了所有操作的平均性能。摊还分析的核心在于，最坏情况下的操作一旦发生了一次，
那么在未来很长一段时间都不会再次发生，这样就会均摊每次操作的代价。
来看下面这个例子，从一个空队列开始，依次执行下面这些操作：push,push,push,pop,pop,pop
单次出队操作最坏情况下的时间复杂度为 O(n)。考虑到我们要做 nn 次出队操作，
如果我们用最坏情况下的时间复杂度来计算的话，那么所有操作的时间复杂度为 O(n^2)。
然而，在一系列的操作中，最坏情况不可能每次都发生，可能一些操作代价很小，另一些代价很高。
因此，如果用传统的最坏情况分析，那么给出的时间复杂度是远远大于实际的复杂度的。
例如，在一个动态数组里面只有一些插入操作需要花费线性的时间，而其余的一些插入操作只需花费常量的时间。
在上面的例子中，出队 操作最多可以执行的次数跟它之前执行过入队操作的次数有关。
虽然一次 出队 操作代价可能很大，但是每 n 次 入队 才能产生这么一次代价为n的出队操作。
因此所有操作的总时间复杂度为：n(所有的入队操作产生） + 2 * n(第一次出队操作产生） + n - 1(剩下的出队操作产生）， 
所以实际时间复杂度为 O(2*n)。于是我们可以得到每次操作的平均时间复杂度为 O(2n/2n)=O(1)。
'''


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
