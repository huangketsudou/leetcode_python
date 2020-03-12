class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        tmp=x^y
        count=0
        while tmp:
            if tmp&1:
                count+=1
            tmp>>=1
        return count


class Solution:
    #xor & (xor - 1)逐个消去最右的1
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')



k=Solution()
print(k.hammingDistance(1,4))
