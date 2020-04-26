from typing import List
import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        tmp=[(0,len(nums))]
        #状态转移方程-dp[i]=max(dp[i-j] for j in range(k+1))+nums[i]
        for i in range(n):
            while tmp[0][1]<i-k:#定长窗口中找到最大/小值的方法
                heapq.heappop(tmp)
            dp[i]=-tmp[0][0]+nums[i]
            heapq.heappush(tmp,(-dp[i],i))
        return max(dp)

k = Solution()
a = [-8269, 3217, -4023, -4138, -683, 6455, -3621, 9242, 4015, -3790]
b = 1
print(k.constrainedSubsetSum(a, b))
print(6455 - 3621 + 9242 + 4015)
