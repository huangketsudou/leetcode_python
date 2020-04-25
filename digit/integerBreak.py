class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return (n-1)*1
        number=[0,1,2,3]
        for i in range(4,n+1):
            product=0
            for j in range(1,i//2+1):
                product=max(product,number[j]*number[i-j])
            number.append(product)
        return number[-1]

import math
class Solution:
    #数学证明法,参见leetcode题解
    #https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

