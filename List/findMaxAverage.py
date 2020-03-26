class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        n = len(nums)
        res=s
        for i in range(k, n):
            s=s+nums[i]-nums[i-k]
            res = max(res, s)
        return res / k
