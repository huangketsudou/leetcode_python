from typing import List
from functools import reduce
import random


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        k = nums[len(nums) // 2]
        for v in nums:
            ans += abs(v - k)
        return ans


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans=0
        median=self.select(nums,0,len(nums)-1,len(nums)//2)
        for v in nums:
            ans+=abs(v-median)
        return ans


    def partition(self, nums, left, right):
        pivotvalue = nums[right]
        i = left
        for j in range(left,right+1):
            if nums[j]<pivotvalue:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i],nums[right]=nums[right],nums[i]
        return i
    def select(self, nums, left, right, k):
        if left == right:
            return nums[left]
        pivot = self.partition(nums, left, right)
        if k == pivot:
            return nums[k]
        elif k < pivot:
            return self.select(nums, left, pivot - 1, k)
        else:
            return self.select(nums, pivot + 1, right, k)
