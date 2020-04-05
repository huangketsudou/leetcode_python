class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<2:return nums
        nums.sort(reverse=True)
        summary=sum(nums)
        end=0
        currentsum=0
        while end<n:
            currentsum+=nums[end]
            if summary-currentsum<currentsum:
                return nums[:end+1]
            end+=1
        return nums
