class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        top=0
        left=[0]*n
        front=[0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    top+=1
                    left[i]=max(left[i],grid[i][j])
                    front[j]=max(front[j],grid[i][j])
        return sum(left)+sum(front)+top
