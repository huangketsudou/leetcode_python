from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        dp = [[float('-inf')]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = max(nums1[i-1]*nums2[j-1]+dp[i-1][j-1], dp[i-1][j], dp[i][j-1],nums1[i-1]*nums2[j-1])
        print(dp)
        return dp[n][m]


class Solution2(object):
    def maxDotProduct(self, A, B):
        if all(a < 0 for a in A) and (b > 0 for b in B): return max(A) * min(B)
        if all(a > 0 for a in A) and (b < 0 for b in B): return min(A) * max(B)

        n,m = len(A), len(B)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1],dp[i-1][j-1] + A[i-1]*B[j-1])
        print(dp)
        return dp[n][m]

k=Solution2()
nums1 = [-3,-8,3,-10,1,3,9]
nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]

g=Solution()
print(g.maxDotProduct(nums1 = [-1,-1], nums2 = [1,1]))
print(k.maxDotProduct(nums1, nums2))
