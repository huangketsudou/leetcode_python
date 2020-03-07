from typing import List
from collections import deque
import heapq
from heapq import heappush,heappop
import functools


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        flag=nums[0]
        for num in nums[1:]:
            flag ^= num

        for i in range(len(nums)+1):
            flag ^= i

        return flag


class Solution:
    #位运算
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


class Solution:
    #哈希表
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

class Solution:
    #排序
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
            
            
            
class Solution:
    #高斯和函数
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum




k=Solution()
print(k.missingNumber([9,6,4,2,3,5,7,0,1]))
