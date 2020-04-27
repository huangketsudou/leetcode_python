class Solution:
    #和那道摔鸡蛋一样的
    def getMoneyAmount(self, n: int) -> int:
        res=self.core(1,n)
        return res


    def core(self,left,right):
        if left>=right:
            return 0
        ans=float('inf')
        for i in range(left,right):
            ans=min(max(self.core(left,i-1),self.core(i+1,right))+i,ans)
        return ans


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp=[[float('inf')]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if i>=j:
                    dp[i][j]=0
        for i in range(n,0,-1):
            for j in range(i,n+1):
                for k in range(i,j):
                    dp[i][j]=min(dp[i][j],max(dp[i][k-1],dp[k+1][j])+k)
        return dp[1][n]


