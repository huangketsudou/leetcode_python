class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums or not nums[0]: return []

        n = len(nums)
        m = len(nums[0])
        if n * m != r * c:
            return nums

        dp = [[0] * c for _ in range(r)]
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                R = idx // c
                C = idx % c
                dp[R][C]=nums[i][j]


        return dp
