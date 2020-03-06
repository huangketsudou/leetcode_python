#题解思路来源-3
#https://leetcode-cn.com/problems/different-ways-to-add-parentheses/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-5-5/

from typing import List
from collections import deque
import heapq
import functools

class Solution:
    @functools.lru_cache(None)
    def diffWaysToCompute(self, input: str) -> List[int]:

        if input.isdigit():return [int(input)]
        result=[]
        for i,opt in enumerate(input):
            if opt in '+-*':
                left=self.diffWaysToCompute(input[:i])
                right=self.diffWaysToCompute(input[i+1:])

                result.extend(self.calculate(opt,l,r) for l in left for r in right)
        return result

    def calculate(self,opt,l,r):
        if opt=='+':
            return l+r
        elif opt=='-':
            return l-r
        elif opt=='*':
            return l*r

class Solution2:
    def diffWaysToCompute(self, input: str):
        # 递归 + 备忘录
        self.formula = input
        self.memo = {}
        return self._diffWaysToCompute(0, len(input))

    def _diffWaysToCompute(self, lo, hi):
        if self.formula[lo:hi].isdigit():
            return [int(self.formula[lo:hi])]
        if((lo, hi) in self.memo):
            return self.memo.get((lo, hi))
        ret = []
        for i, char in enumerate(self.formula[lo:hi]):
            if char in ['+', '-', '*']:
                leftResult = self._diffWaysToCompute(lo, i + lo)
                rightResult = self._diffWaysToCompute(lo + i + 1, hi)
                ret.extend([eval(str(i) + char + str(j)) for i in leftResult for j in rightResult])
                self.memo[(lo, hi)] = ret
        return ret


class Solution3:
    #动态规划-
    def diffWaysToCompute(self, input: str):

        numberList=[]
        optList=[]
        number=0
        for i in input:
            if not i.isdigit():
                optList.append(i)
                numberList.append(number)
                number=0
                continue
            number=number*10+int(i)

        numberList.append(number)

        N=len(numberList)
        print(numberList)
        dp=[[[] for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dp[i][i]=[numberList[i]]

        for n in range(2,N+1):#有几个数字
            for i in range(N):#数字起始编号
                j=i+n-1#数字终止编号
                if j>=N:break
                result=[]
                for s in range(i,j):#s代表符号
                    result1=dp[i][s]
                    result2=dp[s+1][j]
                    for x in result1:
                        for y in result2:
                            opt=optList[s]
                            result.append(self.calculate(opt,x,y))

                dp[i][j] = result

        return dp[0][N-1]

    def calculate(self, opt, l, r):
        if opt == '+':
            return l + r
        elif opt == '-':
            return l - r
        elif opt == '*':
            return l * r


k=Solution3()
print(k.diffWaysToCompute("2*3-4*5"))
