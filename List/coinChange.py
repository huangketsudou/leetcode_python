from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math

from collections import deque




class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:return 0
        saw=[]
        stack=deque()
        stack.append((0,amount))
        while stack:
            result, amount = stack.popleft()
            for coin in coins:
                left = amount - coin
                if left < 0: continue
                if left==0:return result+1
                if left not in saw:
                    stack.append((result + 1, left))
                    saw.append(left)
        return -1


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:return 0
        coins.sort()
        dp=[float('inf')]*(amount+1)
        for i in coins:
            dp[i]=1

        for i in range(coins[0]+1,amount+1):
            for coin in coins:
                if i-coin>0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1


class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1




k=Solution2()
coins=[102,220,186,465,336,107,387,418]
amount=495
print(k.coinChange(coins, amount))
