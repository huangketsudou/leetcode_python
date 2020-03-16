from typing import List
import functools
import math
import itertools


class Solution:
    #flood fill算法-扫雷游戏
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        answer = 0

        def dfs(i, j):
            grid[i][j] = '0'
            if i - 1 >= 0 and grid[i - 1][j] == '1': dfs(i - 1, j)
            if i + 1 < n and grid[i + 1][j] == '1': dfs(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == '1': dfs(i, j - 1)
            if j + 1 < m and grid[i][j + 1] == '1': dfs(i, j + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    answer += 1
                    dfs(i, j)

        return answer


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        answer = 0

        def bfs(i, j):
            island = [(i, j)]
            while island:
                n_i, n_j = island.pop(0)
                grid[n_i][n_j] = '0'
                if n_i - 1 >= 0 and grid[n_i - 1][n_j] == '1': island.append((n_i - 1, n_j))
                if n_i + 1 < n and grid[n_i + 1][n_j] == '1': island.append((n_i + 1, n_j))
                if n_j - 1 >= 0 and grid[n_i][n_j - 1] == '1': island.append((n_i, n_j - 1))
                if n_j + 1 < m and grid[n_i][n_j + 1] == '1': island.append((n_i, n_j + 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    answer += 1
                    bfs(i, j)

        return answer


class Solution3:
    #并查集
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        f = [-1] * n * m
        g = {}

        def find(x):
            if f[x] == -1:
                return x
            f[x] = find(f[x])
            return f[x]

        def union(x, y):
            t1 = find(x)
            t2 = find(y)
            # 这里的目的是防止修改最上级节点的值
            if t1 != t2:
                f[t2] = t1
#------------------------
#并查表另一个写法
        def find2(x):
            g.setdefault(x, x)
            if g[x] != x:
                g[x] = find2(x)
            return g[x]

        def union2(x, y):
            f[find2(x)] = find2(y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    for x, y in [[-1, 0], [0, -1]]:
                        tmp_x, tmp_y = i + x, j + y
                        if 0 <= tmp_x < n and 0 <= tmp_y < m and grid[tmp_x][tmp_y] == '1':
                            union(tmp_x * m + tmp_y, i * m + j)

        res = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res.add(find(i * m + j))
        return len(res)


k = Solution3()
a = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
b = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(k.numIslands(b))
