#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/
#leetcode题解分析



class Solution_inf:
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

    
class Solution_inf1:
    # 不限制交易次数
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxprofit=0
        minprice=float('-inf')
        for i in range(n):
            tmp=maxprofit
            maxprofit=max(maxprofit,minprice+prices[i])
            minprice=max(minprice,tmp-prices[i])
        return maxprofit

class Solution_inf2:
    # 不限制交易次数
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[-1][1]=float('-inf')
        for i in range(n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[n-1][0]    
    

class Solution_1:
    #仅允许交易一次
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprofit=0
        n=len(prices)
        for i in range(n):
            minprice=min(prices[i],minprice)
            maxprofit=max(maxprofit,prices[i]-minprice)
        return maxprofit

    
class Solution_11:
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
    
class Solution_2:
    #限制交易两次
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0]* 2 for _ in range(3)] for _ in range(n)]
        for i in range(n):
            for k in range(2,0,-1):
                if i==0:
                    dp[i][k][0]=0
                    dp[i][k][1]=-prices[i]
                    continue
                dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        return dp[n-1][2][0]
    

    
class Solution:
    #限制交易次数为k
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k==0:return 0
        if k > n // 2:
            maxprofit = 0
            minprice = float('-inf')
            for i in range(n):
                tmp = maxprofit
                maxprofit = max(maxprofit, minprice + prices[i])
                minprice = max(minprice, tmp - prices[i])
            return maxprofit
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for l in range(1,k+1):
                if i == 0:
                    dp[i][l][0] = 0
                    dp[i][l][1] = -prices[i]
                    continue
                dp[i][l][0] = max(dp[i - 1][l][0], dp[i - 1][l][1] + prices[i])
                dp[i][l][1] = max(dp[i - 1][l][1], dp[i - 1][l - 1][0] - prices[i])
        return dp[n - 1][k][0]    
    
class Solution_cool:
    # 不限制交易次数，冷静期
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]#加1是为了避免出现[1]这样的数组导致索引出错
        dp[0][1]=float('-inf') #0是初始状态，索引修改这里的dp[-1][1]为dp[0][1]
        for i in range(1,n+1):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i])
        return dp[n][0]


class Solution_cool2:
    # 不限制交易次数
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        pre_selled,pre_bought=0,float('-inf')
        last_selled=0
        for i in prices:
            tmp=pre_selled
            pre_selled=max(pre_selled,pre_bought+i)
            pre_bought=max(pre_bought,last_selled-i)
            last_selled=tmp
        return pre_selled


k=Solution()
print(k.maxProfit([7,1,5,3,6,4]))
