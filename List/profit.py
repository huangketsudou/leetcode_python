#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/
#leetcode题解分析



class Solution:
    #不限制交易次数
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        n=len(prices)
        left=prices[0]
        right=prices[0]
        answer=0
        for i in range(1,n):
            if prices[i]<right:
               answer+=(right-left)
               left=right=prices[i]
            else:
                right=prices[i]
        answer+=max(0,right-left)
        return answer



class Solution2:
    #仅允许交易一次
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprofit=0
        n=len(prices)
        for i in range(n):
            minprice=min(prices[i],minprice)
            maxprofit=max(maxprofit,prices[i]-minprice)
        return maxprofit

    
class Solution3:
    #仅允许交易一次
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        n=len(prices)
        dp=[[0]*2 for _ in range(n)]
        #base case
        for i in range(n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],-prices[i])
        return dp[n-1][0]
    
    

k=Solution()
print(k.maxProfit([7,1,5,3,3,6,4]))
