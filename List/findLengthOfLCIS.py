class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:return n
        left=0
        right=1
        res=0
        while right<n:
            if nums[right]<=nums[right-1]:
                res=max(res,right-left)
                left=right
            right+=1
        res=max(right-left,res)
        return res
