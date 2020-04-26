from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        if n==0:return []
        stack=deque()
        ans=[]
        i=1
        stack.append(nums[0])
        while stack:
            stacksecond=deque()
            while stack:
                l=stack.popleft()
                ans.append(l.pop(0))
                if len(l)!=0:
                    stacksecond.append(l)
            stack=stacksecond
            if i<n:
                stack.appendleft(nums[i])
                i+=1
        return ans
