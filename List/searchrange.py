from typing import List



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n<1:
            return [-1,-1]
        answer=[-1,-1]
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if target<=nums[mid]:
                right=mid-1
            else:
                left=mid+1
        if left<n and nums[left]==target:
            answer[0]=left
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if target>=nums[mid]:
                left=mid+1
            else:
                right=mid-1
        if right>=0 and nums[right]==target:
            answer[1]=right
        return answer





k=Solution()
print(k.searchRange([1],1))
