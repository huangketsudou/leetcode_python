from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans=[]

        def core(number,n):
            if number>n:
                return
            ans.append(number)
            for i in range(10):
                core(number*10+i,n)

        for i in range(1,10):
            core(i,n)

        return ans

from collections import deque

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        stack=deque()
        for i in range(9,0,-1):
            if i<=n:
                stack.append(i)
        ans=[]
        while stack:
            number=stack.pop()
            ans.append(number)
            for j in range(9,-1,-1):
                if number*10+j<=n:
                    stack.append(number*10+j)
        return ans
