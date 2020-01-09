from typing import List



class Solution:
    #bfs
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


    
    
class Solution:
    #dfs
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        # 记录
        visited = set()
        # 建图
        for x, y in prerequisites:
            graph[y].append(x)

        # 深度遍历
        def dfs(i, being_visited):
            if i in being_visited: return False
            if i in visited: return True
            visited.add(i)
            being_visited.add(i)
            for j in graph[i]:
                if not dfs(j, being_visited): return False
            being_visited.remove(i)
            return True
        # 检测每门功课起始是否存在环
        for i in range(numCourses):
            # 已经访问过
            if i in visited: continue
            if not dfs(i, set()): return False
        return True



k=Solution()
print(k.canFinish(4,[[1,0],[2,1],[0,2],[0,3]]))
