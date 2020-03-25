class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        n, m = len(grid), len(grid[0])
        leftstack = [0] * n#左边上一次的高度
        frontstack = [0] * m#正面上一次的高度
        res = 0
        for i in range(n):
            for j in range(m):
                res+=max(0,grid[i][j]-frontstack[j])
                frontstack[j]=grid[i][j]
                res+=max(0,grid[i][j]-leftstack[i])
                leftstack[i]=grid[i][j]
                if grid[i][j]!=0:#顶层
                    res+=1
        return res*2


k = Solution()
print(k.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
