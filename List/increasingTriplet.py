from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        stack = [nums[0]]
        for i in range(1, n):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
                if len(stack) == 3: return True
            else:
                j = len(stack) - 1
                while j > 0 and stack[j - 1] >= nums[i]:
                    j -= 1
                stack[j] = nums[i]
        return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        small = float('inf')
        mid = float('inf')
        #这里会出现small比mid大的情况，但是他隐含了一个条件是，有一个比 small 大比 mid 小的前·最小值出现在 mid 之前
        for i in nums:
            if i <= small:
                small = i
            elif i <= mid:
                mid = i
            elif i > mid:
                return True
        return False
