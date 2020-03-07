from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        left,right=0,0
        while right<n-1:
            if nums[left]==0:
                while right<n-1 and nums[right]==0:
                    right+=1
                nums[left],nums[right]=nums[right],nums[left]
            left+=1

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

k=Solution()
k.moveZeroes([0,1,0,3,12])
