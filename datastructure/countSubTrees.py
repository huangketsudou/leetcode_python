from typing import List
from collections import defaultdict, Counter


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        tree = defaultdict(Counter)
        for edge in edges:
            start, end = edge
            graph[start].append(end)
        for i in range(len(labels) - 1, -1, -1):
            c = Counter()
            c.setdefault(labels[i], 1)
            if i not in graph:
                tree[i] = c
            else:
                for sub in graph[i]:
                    c += tree[sub]
                tree[i] = c
        result = []
        for i in range(len(labels)):
            result.append(tree[i].get(labels[i]))
        return result


class Solution1:

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.ans = [0] * len(labels)
        graph = defaultdict(list)
        for edge in edges:
            start, end = edge
            graph[start].append(end)
            graph[end].append(start)
        self.dfs(set(),graph,0,labels)
        return self.ans

    def dfs(self, visited, graph, node, labels):
        c = Counter()
        c.setdefault(labels[node], 1)
        visited.add(node)
        for op in graph[node]:
            if op not in visited:
                oldtree = self.dfs(visited, graph, op, labels)
                c += oldtree
        visited.remove(node)
        self.ans[node] = c[labels[node]]
        return c


k = Solution1()
print(k.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))
