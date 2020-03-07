class PeekingIterator:
    #本质上就是在peek的时候就进行指针的移动，并且保留弹出来的值
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.Iterator=iterator
        self.prev=None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.prev:
            return self.prev
        else:

            tmp=self.Iterator.next()
            self.prev=tmp
            return tmp


    def next(self):
        """
        :rtype: int
        """
        if self.prev:
            nxt=self.prev
            self.prev=None
            return nxt
        else:
            return self.Iterator.next()


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.prev:
            return True
        if self.Iterator.hasNext():
            return True
        return False
