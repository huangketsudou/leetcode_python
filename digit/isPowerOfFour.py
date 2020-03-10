class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1

class Powers:
    def __init__(self):
        max_power = 15
        self.nums = nums = [1] * (max_power + 1)
        for i in range(1, max_power + 1):
            nums[i] = 4 * nums[i - 1]

class Solution:
    p = Powers()
    def isPowerOfFour(self, num: int) -> bool:
        return num in self.p.nums

from math import log2
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0

class Solution:
#检查最后一个1出现在偶数位
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0

class Solution {
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1

#题解原理
#https://leetcode-cn.com/problems/power-of-four/solution/4de-mi-by-leetcode/
