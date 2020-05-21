from typing import List


class Solution:
    #利用先后手的差值表示两者分数的大小
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        return self.dfs(nums,0,n-1,1)>=0


    def dfs(self,nums,left,right,turn):
        if left==right:return turn*nums[left]
        a=turn*nums[left]+self.dfs(nums,left+1,right,-turn)
        b=turn*nums[right]+self.dfs(nums,left,right-1,-turn)
        return max(a,b)


class Solution:
    #利用先后手的差值表示两者分数的大小
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=nums[i]
                else:
                    dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
        return dp[0][n-1]>=0