from typing import List
import functools


class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer=nums[0]
        n=len(nums)
        i=1
        while i <n:
            if nums[i]<answer:
                return nums[i]
            i+=1
        return answer



class Solution2:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid
            else:
                right=right-1
        return nums[left]



k=Solution()
print(k.findMin([1,1,1,1,1,1,1,1]))
