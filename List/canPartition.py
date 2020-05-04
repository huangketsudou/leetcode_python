from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summary = sum(nums)
        if summary & 1: return False
        target = summary // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        for i in range(n):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[-1][-1]


class Solution:
    #参考combinationSum4.py的解释，参考leetcode377的题解区
    def canPartition(self, nums: List[int]) -> bool:
        summary = sum(nums)
        if summary & 1: return False
        target = summary // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True
        j = 0
        while j < n:
            for i in range(target,0,-1):
                if i-nums[j]>=0:
                    dp[i] = dp[i] or dp[i - nums[j]]
            j += 1
        return dp[-1]


class Solution:
    #dfs搜索的目标是该数要不要用
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        div, mod = divmod(_sum, 2)
        if mod or max(nums) > div: return False
        nums.sort(reverse=True)
        target = [div] * 2 #一个要取一个不要取
        return self.dfs(nums, 0, target)

    def dfs(self, nums, index, target):
        for i in range(2):
            if target[i] >= nums[index]:
                target[i] -= nums[index]
                if target[i] == 0 or self.dfs(nums, index + 1, target): return True
                target[i] += nums[index]
        return False