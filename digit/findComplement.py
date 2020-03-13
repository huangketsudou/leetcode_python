class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = 1
        while temp < num:
            temp <<= 1
            temp += 1
        return temp ^ num


class Solution:
    def findComplement(self, num: int) -> int:
        import math
        k=int(math.log2(num))+1
        return 2**k-1-num
