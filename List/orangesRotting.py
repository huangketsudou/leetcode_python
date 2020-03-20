class Solution:
    #通过广度优先搜索以及修改原数组实现遍历
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def neighbors(i,j):
            for nr, nc in ((i-1,j),(i,j-1),(i+1,j),(i,j+1)):
                if 0 <= nr < n and 0 <= nc < m:
                    yield nr, nc


        n, m = len(grid), len(grid[0])
        rot=deque()
        d=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]==2:
                    rot.append((r,c,d))


        while rot:
            x,y,d=rot.popleft()
            for nx,ny in neighbors(x,y):
                if grid[nx][ny]==1:
                    grid[nx][ny]=2
                    rot.append((nx,ny,d+1))

        if any(1 in row for row in grid):
            return -1
        return d



k=Solution()
print(k.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
