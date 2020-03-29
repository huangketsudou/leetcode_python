class Solution:
    #BFS遍历
    def maxDistance(self, grid: List[List[int]]) -> int:
        land=deque()
        n,m=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    land.append((i,j,0))
        res=0
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        while land:
            x,y,dis=land.popleft()
            # grid[x][y]=1  #最初的想法是放在这里，意思是当以该点为起点时就将该点置为陆地
            #但这样的做法产生了一个问题，就是由于是在访问玩其他的点后再访问下一层，因此导致该点被重复加入数组多次
            如[[0,1,0,0],
              [[1,0,0,1],
              [[0,1,0,0]]  中间的点(1,1)处，被重复加入了3次，而点(1,2)被加入了一次，再广度遍历(1,1)的周围时，又将(1,2)加入了3次，
             #所以造成max计算中的错误，得到不正确的结果
            res=max(res,dis)
            for dx,dy in direction:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
                    land.append((nx,ny,dis+1))
                    grid[nx][ny]=1
        return res if res>0 else -1

class Solution:
    #动态规划
    def maxDistance(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp=[[float('inf')]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i>=1:dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
                    if j>=1:dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if grid[i][j]==0:
                    if i+1<n:dp[i][j]=min(dp[i][j],dp[i+1][j]+1)
                    if j+1<m:dp[i][j]=min(dp[i][j],dp[i][j+1]+1)
        ans=-1
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=1:
                    ans=max(dp[i][j],ans)
        return ans if ans!=float('inf') else -1


k=Solution()
a=[[1,0,1],[0,0,0],[1,0,1]]
b=[[1,0,0],[0,0,0],[0,0,0]]
c=[[1,1,1],[1,1,1],[1,1,1]]
d=[[0,0,0],[0,0,0],[0,0,0]]
e=[[1,0,0,0,0,1,0,0,0,1],[1,1,0,1,1,1,0,1,1,0],[0,1,1,0,1,0,0,1,0,0],[1,0,1,0,1,0,0,0,0,0],[0,1,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,0,1],[0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,1,1,0,0],[1,1,0,1,1,1,1,1,0,0]]
print(k.maxDistance(e))
