from typing import List
from collections import defaultdict,deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        outnode = defaultdict(list)
        innode = defaultdict(list)
        for start,end in connections:
            outnode[start].append(end)
            innode[end].append(start)
        stack = deque()
        stack.append(0)
        visited = set()
        ans = 0
        while stack:
            node = stack.popleft()
            if node in outnode:
                for k in outnode[node]:
                    if k not in visited:
                        stack.append(k)
                        ans += 1
            if node in innode:
                for g in innode[node]:
                    stack.append(g)
            visited.add(node)
        return ans

k=Solution()
print(k.minReorder(n = 3, connections = [[1,0],[2,0]]))