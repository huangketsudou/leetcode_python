from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        start = 0
        while start < n:
            if start + nums[start] >= n - 1: return result + 1
            big = bigid = 0
            i = start + 1
            while i < n and i < start + nums[start] + 1:#一次跳跃的过程中，找到下一次跳跃可能的最大值
                if nums[i] + i>= big+bigid:
                    big = nums[i]
                    bigid = i
                i += 1
            result += 1
            start = bigid


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        left, right, count = 0, 0, 0
        maxpos=0
        while left < n - 1:
            maxpos=max(maxpos,left+nums[left])
            if left==right:
                right=maxpos
                count+=1
            left+=1
        return count


class Solution2:
    def jump(self, nums: List[int]) -> int:
        if nums.count(1)==len(nums):
            return len(nums)-1
        def fun(n):
            if not n:
                return 0
            for k,v in enumerate(n):
                if v>=len(n)-k:
                    return fun(n[:k])+1
        return fun(nums[:-1])



k = Solution()
print(k.jump([1]))
