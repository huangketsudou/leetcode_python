from typing import List
import heapq
from itertools import product
import itertools

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans=list()
        for i in product(nums1,nums2):
            ans.append(i)
        res=heapq.nsmallest(k,ans,key=sum)
        return list(map(list,res))

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]

class Solution:
    #设置一个以和为优先的队列，输出队头，当j为0时，加入下一行
    '''
    [[1,1,1,0,*,*,*]
    [1,1,0,*,*,*,*]
    [1,0,*,*,*,*,*]
    [0,*,*,*,*,*,*]
    [*,*,*,*,*,*,*]]
    就像这样，空间复杂度，O(m),时间复杂度O(klog(m))
    '''
    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs

