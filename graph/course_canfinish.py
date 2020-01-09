from typing import List



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #实际上是一道探讨有向非循环图的题目
        from collections import defaultdict
        count = defaultdict(int)
        for i in range(numCourses):
            count[i] = 0
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[j].append(i)
            count[i] += 1
        ready=[]
        for k,v in count.items():
            if v==0:
                ready.append(k)
        topo=[]
        while ready:
            u=ready.pop()
            topo.append(u)
            for e in graph[u]:
                count[e]-=1
                if count[e]==0:
                    ready.append(e)
        return len(topo)==numCourses



k=Solution()
print(k.canFinish(4,[[1,0],[2,1],[0,2],[0,3]]))
