class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]




import heapq
from heapq import heappop,heapify,heappush


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k==0:return []
        hp=[-x for x in arr[:k]]
        heapq.heapify(hp)
        for num in arr[k:]:
            if -hp[0]>num:
                heappop(hp)
                heappush(hp,-num)
        ans=[-x for x in hp]
        return ans
