class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        n=len(nums)
        left,right=0,n-1
        while left<right:
            middle=(left+right)>>1
            if nums[middle]<target:
                left=middle+1
            else:
                right=middle
        return left if nums[left]==target else -1
