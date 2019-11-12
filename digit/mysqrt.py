from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0]:
            return x
        small=0
        big=x//2+1
        while small<big:
            mid = (big + small+1) // 2
            if mid==small or mid*mid==x:
                return mid
            elif mid*mid>x:
                big=mid-1
            else:
                small=mid
        return big


class Solution2:
    def mySqrt(self, x: int) -> int:
        # 为了照顾到 0 把左边界设置为 0
        left = 0
        # 为了照顾到 1 把右边界设置为 x // 2 + 1
        right = x // 2 + 1
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left




k=Solution()
print(k.mySqrt(8))
