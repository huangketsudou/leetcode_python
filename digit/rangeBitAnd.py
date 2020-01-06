from typing import List
import functools
import math
import itertools


class Solution:
    '''
    可以这样理解，将两个数写为具有相同位数的二进制数，不足的补零，
    很明显范围内只要有一个数的某一位二进制是0，那么结果的这一位就一定是0，
    对m，n两个数从高位向地位检查，两个数这一位都为1时，范围内所有数这一位为1，
    如果这两个数这一位互异，那么余下的范围与必为0，如0b1111和0b0111
    '''

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0: return 0
        if m == n: return m
        answer = m
        for i in range(m + 1, n + 1):
            answer &= i
            if answer == 0:
                return answer
        return answer


class Solution2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 上面的分析可知，最后的结果一定<=m，这里的思路相当于从后往前计算n里面各位的1
        if m == 0: return 0
        while m < n:
            n &= n - 1
        return n


k = Solution()
print(k.rangeBitwiseAnd(0b111, 0b1111))
