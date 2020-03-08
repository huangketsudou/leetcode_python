from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math
from collections import deque


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:return n
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)

#https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/

class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res



k=Solution()
print(k.lengthOfLIS([10,9,2,5,3,7,101,18]))
