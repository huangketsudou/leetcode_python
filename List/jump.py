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
            while i < n and i < start + nums[start] + 1:
                if nums[i] + i>= big+bigid:
                    big = nums[i]
                    bigid = i
                i += 1
            result += 1
            start = bigid


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
