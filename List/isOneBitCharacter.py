class Solution(object):
    def isOneBitCharacter(self, bits):
        #检查最后两个0之间1的个数是否为奇数
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0

class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
