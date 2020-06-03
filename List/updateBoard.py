from typing import List
from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = len(board), len(board[0])
        self.dp = self.searchMine(board)
        self.visited = [[False] * col for _ in range(row)]
        ans = board.copy()
        x, y = click
        if board[x][y] == 'M':
            ans[x][y] = 'X'
            return ans
        self.dfs(board,ans,x,y)
        return ans

    def searchMine(self, board):
        row, col = len(board), len(board[0])
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                count = 0
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if 0 <= i + dx < row and 0 <= j + dy < col and board[i + dx][j + dy] == 'M':
                        count += 1
                dp[i][j] = count
        return dp

    def dfs(self, board, ans, x, y):
        row, col = len(ans), len(ans[0])
        node = deque()
        node.append((x, y))
        while node:
            x, y = node.popleft()
            self.visited[x][y] = True
            ans[x][y] = 'B' if self.dp[x][y] == 0 else str(self.dp[x][y])
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if self.dp[x][y] == 0 and 0 <= x + dx < row and 0 <= y + dy < col and not self.visited[x + dx][y + dy] and board[x + dx][y + dy] != 'M':
                    node.append((x + dx, y + dy))


a =[['E', 'E', '1', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']]

k=Solution()
print(k.updateBoard(a,[3,0]))


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        a, b = click
        if board[a][b] == 'M':
            board[a][b] = 'X'
        elif board[a][b] == 'E':
            d = [*itertools.product((-1, 0, 1), repeat=2)]
            q, v, m, n = [(a, b)], {(a, b)}, len(board), len(board[0])
            while q:
                p = []
                for i, j in q:
                    c, t = 0, []
                    for di, dj in d:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n:
                            c += board[x][y] == 'M'
                            (x, y) not in v and t.append((x, y))
                    board[i][j] = c and str(c) or p.extend(t) or v.update(t) or 'B'
                q = p
        return board

