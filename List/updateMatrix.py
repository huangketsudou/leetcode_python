from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n,m =len(matrix),len(matrix[0])
        stack=deque()
        for i,row in enumerate(matrix):
            for j,v in enumerate(row):
                if v==0:
                    stack.append((i,j,0))
        ans=[[0]*m for _ in range(n)]
        while stack:
            x,y,depth=stack.popleft()
            for dx,dy in direction:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and matrix[nx][ny]==1:
                    ans[nx][ny]=depth+1
                    stack.append((nx,ny,depth+1))
                    matrix[nx][ny]=0
        return ans