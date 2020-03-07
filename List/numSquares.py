from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math

class Solution:
    def __init__(self):
        self.result=float('inf')


    def numSquares(self, n: int) -> int:

        def core(number,recored):

            if number==0:
                self.result=min(self.result,recored)
            for i in range(1,int(math.sqrt(number))+1):
                core(number-i**2,recored+1)

        core(n,0)
        return int(self.result)

class Solution2:
    #BFS
    def numSquares(self, n: int) -> int:
        stack=deque()
        stack.append((0,n))
        visited=set()
        visited.add(n)#缺乏这个剪枝会超出内存
        while stack:
            result,number=stack.popleft()
            for i in range(1,int(math.sqrt(number)+1)):
                k=number-i**2
                if k==0:return result+1
                if k not in visited:#减少重复树枝的计算
                    stack.append((result+1,k))
                    visited.add(k)


class Solution3:
    #动态规划，dp[i]表示构成i需要的最少个数
    #初始化各位最多即全为1构成对于i，便利i=[2,n]的区间
    #对于dp[i]，遍历区间[1,int(sqrt(i))+1)的空间，规划函数为dp[i]=min(dp[i],dp[i-j*j]+1)
    def numSquares(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[-1]


class Solution4:
    #费马四数和定理-https://zhuanlan.zhihu.com/p/104030654
    def numSquares(self,n):
        if int(math.sqrt(n))**2==n:return 1
        while n%4==0:
            n=n//4
        if ((n-7)%8)==0:
            return 4
        for i in range(1,int(math.sqrt(n))+1):
            y=int(math.sqrt(n-i**2))
            if y**2+i**2==n:return 2
        return 3


k=Solution2()
print(k.numSquares(13))
