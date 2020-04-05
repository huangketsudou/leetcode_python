
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n=len(A)
        if n==0:return A
        m=len(A[0])
        dp=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j]=A[j][i]
        return dp
