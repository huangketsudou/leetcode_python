#思路是维护一个最大堆和一个最小堆，两者的堆顶均值或者最大堆堆顶就是结果
#要求最小堆中的元素全部小于


from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        heappush(self.maxheap, num)
        endelement = heappop(self.maxheap)
        heappush(self.minheap, -endelement)
        if self.size & 1:
            headelement=-heappop(self.minheap)
            heappush(self.maxheap,headelement)


    def findMedian(self) -> float:
        if self.size==0:return 0
        if self.size & 1:
            return self.maxheap[0]
        else:
            return (self.maxheap[0]-self.minheap[0])/2
        

