from typing import List
import functools
import math
import itertools


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.head = root
        self.travel = self.ordertravel()
        self.length = len(self.travel)
        self.cur = 0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.cur += 1
        return self.travel[self.cur - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.cur < self.length

    def ordertravel(self):
        cur = self.head
        stack = []
        numbers = []
        while cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop(-1)
            numbers.append(node.val)
            cur = node.right
        return numbers


class BSTIterator2:

    def __init__(self, root: TreeNode):
        self.head = root
        self.stack = []
        self.cur = self.ordertravel(self.head)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.cur is None:
            return None
        answer = self.cur.val
        self.cur = self.cur.right
        self.cur = self.ordertravel(self.cur)
        return answer

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0 or (self.cur is not None)

    def ordertravel(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        return self.stack.pop(-1) if len(self.stack) else None


T7 = TreeNode(7)
T3 = TreeNode(3)
T15 = TreeNode(15)
T9 = TreeNode(9)
T20 = TreeNode(20)
T7.left = T3
T7.right = T15
T15.left = T9
T15.right = T20

k = BSTIterator2(T7)
