class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prev = 0
        n = len(nums)
        if n<1:return -1
        cunsum = [0] * n
        for i in range(n):
            cunsum[i] = prev + nums[i]
            prev = cunsum[i]
        cunsum=[0]+cunsum+[cunsum[-1]]
        for i in range(1,n+1):
            if cunsum[i-1]==cunsum[-1]-cunsum[i]:
                return i-1
        return -1
