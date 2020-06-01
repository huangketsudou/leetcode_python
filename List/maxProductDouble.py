from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        print()
        return max((nums[0] - 1) * (nums[1] - 1), (nums[-2] - 1) * (nums[-1] - 1))


k=Solution()
print(k.maxProduct([3,4,5,2]))
