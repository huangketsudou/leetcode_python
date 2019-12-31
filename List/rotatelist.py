from typing import List
import functools
import math
import itertools


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k >= n:
            k = k % n
        i = n - k
        while i < n:
            l = i
            while l > k - n + i:
                nums[l - 1], nums[l] = nums[l], nums[l - 1]
                l -= 1
            i += 1


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        tmp = nums[n - k:]
        nums[k:] = nums[:n - k]
        nums[:k] = tmp


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0: return
        start = 0
        tmp = nums[start]
        cnt = 0
        while cnt < n:
            nxt = (start + k) % n
            while nxt != start:
                nums[nxt], tmp = tmp, nums[nxt]
                nxt = (nxt + k) % n
                cnt += 1
            nums[nxt] = tmp
            start += 1
            tmp = nums[start]
            cnt += 1


k = Solution3()
b = [1, 2, 3, 4, 5, 6]
k.rotate(b, 2)
print(b)
