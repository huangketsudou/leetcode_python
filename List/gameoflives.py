class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m=len(board),len(board[0])
        neighbors=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(n):
            for j in range(m):
                neighlive=0
                for dx,dy in neighbors:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<n and 0<=nj<m and  (board[ni][nj] % 2 == 1):
                        neighlive+=1
                if board[i][j]==1 and (neighlive>3 or neighlive<2):
                    board[i][j]+=2
                if board[i][j]==0 and neighlive==3:
                    board[i][j]+=2
        for i in range(n):
            for j in range(m):
                if board[i][j]==2:
                    board[i][j]=1
                elif board[i][j]==3:
                    board[i][j]=0
