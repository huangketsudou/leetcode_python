from typing import List
from collections import deque


class Solution:
    #思路：减一后全为1
    def isPowerOfTwo(self, n: int) -> bool:

        if n==1:
            return True

        strnum=bin(n-1)[2:]
        return strnum=='1'*len(strnum)


class Solution2:
    #思路：n-1后，最高位变为0，其余全为1，与n相反
    def isPowerOfTwo(self, n: int) -> bool:

        return n>0 and n & (n-1) ==0


class Solution3:
    #思路：对于一个数，-n在变为补码表示时，除最右边的1之外，其余全部取反，
    #因此对于这题可以用这样的方法
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n


k=Solution2()
print(k.isPowerOfTwo(0))
