from typing import List
from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.ans=0
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for start, end in edges:
            tree[start].append(end)

        def dfs(node):
            if len(tree[node]) == 0 and not hasApple[node]:
                return False
            elif len(tree[node]) == 0 and hasApple[node]:
                return True
            had = hasApple[node]
            for i in tree[node]:
                child = dfs(i)
                had |= child
                if child:
                    self.ans+=2
            return had
        dfs(0)
        return self.ans


k = Solution()
print(k.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
