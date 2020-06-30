from typing import List


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        y = self.find(self.parents[x])
        self.parents[x] = y
        return y

    def union(self, x1, x2):
        y1, y2 = self.find(x1), self.find(x2)
        if y1 == y2:
            return
        if self.rank[y1] <= self.rank[y2]:
            self.parents[y1] = y2
        else:
            self.parents[y2] = y1
        if self.rank[y1] == self.rank[y2]:
            self.rank[y2] += 1

class Solution:
    def kruskal(self, n, edges, skip_edge=None):
        uf = UnionFind(n)
        cost = edges_cnt = 0
        if skip_edge is not None:
            v1, v2, w = skip_edge
            cost, edges_cnt = w, 1
            uf.union(v1, v2)
        for v1, v2, w in edges:
            if uf.find(v1) == uf.find(v2):
                continue
            cost += w
            edges_cnt += 1
            uf.union(v1, v2)
            if edges_cnt == n - 1:
                break
        return cost if edges_cnt == n - 1 else float("inf")

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indices = sorted(range(len(edges)), key=lambda x: edges[x][2])
        edges = [edges[x] for x in indices]
        min_cost = self.kruskal(n, edges)
        ans = [[], []]
        for i in range(len(edges)):
            skip_edge = edges[i]
            new_edges = edges[:i]+edges[i+1:]
            if self.kruskal(n, new_edges) > min_cost:
                ans[0].append(indices[i])
            elif self.kruskal(n, new_edges, skip_edge) == min_cost:
                ans[1].append(indices[i])
        return ans
