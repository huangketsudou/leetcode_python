from typing import List
from collections import deque


class Solution:
    #单调栈，调用两次
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not n:
            return []
        stack = deque()
        nums = nums + nums
        ans = [-1] * n * 2
        for i, num in enumerate(nums):
            while len(stack) and nums[stack[-1]] < num:
                idx = stack.pop()
                ans[idx] = num
            stack.append(i)
        return ans[:len(ans) // 2]
