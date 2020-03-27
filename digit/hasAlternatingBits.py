class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n&1
        while n > 1:
            b = (n>>1)&1
            if a == b:
                return False
            a = b
            n >>= 1
        return True
        
 
 
 class Solution:
    #将n右移一位并异或n，检查是否全为1
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = n^(n>>1)
        return tmp&(tmp+1) == 0
