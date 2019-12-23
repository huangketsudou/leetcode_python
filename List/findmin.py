from typing import List
import functools


class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer = nums[0]
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] < nums[0]:
                return nums[i]
            i += 1
        return answer


class Solution2:
    # 不要从左边入手，有边界问题，当mid>small时，不能够确定此时的small-big之间是否为旋转数组
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        small, big = 0, n - 1
        while small < big:
            mid = (small + big) // 2
            if nums[mid] > nums[big]:
                small = mid - 1
            else:
                big = mid
        return nums[small]


class Solution3:
    # 可以用来找最大值
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        small, big = 0, n - 1
        while small < big:
            mid = (small + big + 1) // 2
            if nums[mid] > nums[small]:
                small = mid
            else:
                big = mid - 1
        return nums[small]


k = Solution3()
print(k.findMin([3, 4, 5, 0, 1, 2]))
