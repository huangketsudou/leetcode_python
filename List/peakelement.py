from typing import List
import functools


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        stack = [float('-inf')]
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] >= stack[-1]:
                stack.append(nums[i])
            else:
                return i - 1
            i += 1
        return n - 1


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        #利用局部递增或者递减信息，mid与其右侧比较，直到找到只剩一个
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid]>nums[mid+1]:
                right=mid
            else:
                left=mid+1
        return left


k = Solution()
print(k.findPeakElement([1]))
