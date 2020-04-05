from typing import List
import functools


class Node:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self._cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def __removenode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def __addnode(self, node):
        hnext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = hnext
        hnext.prev = node

    def __movetohead(self, node):
        self.__removenode(node)
        self.__addnode(node)

    def __poptail(self):
        node = self.tail.prev
        self.__removenode(node)
        return node

    def get(self, key: int) -> int:
        node = self._cache.get(key, None)
        if not node: return -1
        self.__movetohead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self._cache.get(key)
        if not node:
            newnode = Node()
            newnode.key = key
            newnode.val = value
            self._cache[key] = newnode
            self.__addnode(newnode)
            self.size += 1
            if self.size > self.capacity:
                tail=self.__poptail()
                del self._cache[tail.key]
                self.size-=1
        else:
            node.val=value
            self.__movetohead(node)




from collections import OrderedDict

class LRUCache2(OrderedDict):

    def __init__(self,capacity):
        self.capacity=capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]


    def put(self,key,value):
        if key in self:
            self.move_to_end(key)
        self[key]=value
        if len(self)>self.capacity:
            self.popitem(last=False)
