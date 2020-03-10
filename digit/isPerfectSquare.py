from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math
from collections import deque
from collections import Counter

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        p=1
        while p<num:
            if p**2==num:return True
            if p**2>num:return False
            p+=1


class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:return True
        left,right=1,num//2

        while left<=right:
            midlle=(left+right)//2
            if midlle**2 == num:
                return True
            elif midlle**2 >num:
                right=midlle-1
            else:
                left=midlle+1
        return False


class Solution3:
    #利用了完全平方数的性质，完全平方数可以写为连续奇数的和
    def isPerfectSquare(self, num: int) -> bool:
        num1=1
        while num>0:
            num-=num1
            num1+=2
        return num==0


class Solution4:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num





k=Solution()
print(k.isPerfectSquare(4))


