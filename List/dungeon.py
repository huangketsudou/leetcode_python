from typing import List
import functools
import math
import itertools


class Solution:
    #从右下角遍历，寻找索要保持的最小的生命值
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp=[[0]*n for _ in range(m)]
        dp[-1][-1]=max(1-dungeon[-1][-1],1)
        for i in range(n-2,-1,-1):
            dp[-1][i]=max(1,dp[-1][i+1]-dungeon[-1][i])
        for i in range(m-2,-1,-1):
            dp[i][-1]=max(1,dp[i+1][-1]-dungeon[i][-1])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]



k = Solution()
print(k.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
