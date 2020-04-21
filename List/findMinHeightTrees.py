from typing import List
from collections import defaultdict,deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:return [0]
        d=defaultdict(set)
        for start,end in edges:
            d[start].add(end)
            d[end].add(start)
        q=[k  for k,v in d.items() if len(v)==1]
        while n>2:
            t=[]
            for i in q:
                j=d[i].pop()
                d[j]-={i}
                if len(d[j])==1:
                    t.append(j)
                n-=1
            q=t
        return list(q)

