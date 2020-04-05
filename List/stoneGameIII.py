class Solution:
    #解题思路：动态规划，定义dp[i]为剩下i到n个石头时，当前用户能拿到的最大可能值
    #对于dp[n-1],该用户只能拿走，对于其他的i，下一次用户选择时可以选择的可能情况为dp[i+1],dp[i+2],dp[i+3]三种情况
    #那么当下一个用户拿走了他的最大值之后，剩下的就是我们的分数，为了保证当前我们的分数是最大的，我们应该保证，
    # 下一个用户他能拿到的最大值是这三种情况中最小的，所以状态转移公示为
    #dp[i]=sum(i,n)-min(dp[i+1],dp[i+2],dp[i+3])
    def stoneGameIII(self, s: List[int]) -> str:
        n=len(s)
        dp=[0]*(n+1)+[float('inf')]*4
        sum=0
        for i in range(n-1,-1,-1):
            sum+=s[i]
            choose=min(dp[i+1],dp[i+2],dp[i+3])
            dp[i]=sum-choose
        if sum-dp[0]>dp[0]:
            return 'Bob'
        elif sum-dp[0]<dp[0]:
            return 'Alice'
        else:
            return 'Tie'
