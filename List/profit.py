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

k=Solution()
print(k.maxProfit([7,1,5,3,3,6,4]))
