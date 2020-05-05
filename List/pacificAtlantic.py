from typing import List


class Solution:
    # 从边界入手
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        row, col = len(matrix), len(matrix[0])
        setpa = set()
        setat = set()

        def dfs(i, j, res):
            res.add((i, j))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + dx
                y = j + dy
                if 0 <= x < row and 0 <= y < col and matrix[x][y] >= matrix[i][j] and (x, y) not in res:
                    dfs(x, y, res)

        for i in range(row):
            dfs(i, 0, setpa)
        for j in range(col):
            dfs(0, j, setpa)
        for i in range(row):
            dfs(i, col - 1, setat)
        for j in range(col):
            dfs(row - 1, j, setat)
        ans=setpa & setat
        return list(map(list,ans))
