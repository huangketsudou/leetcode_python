class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            strnum = str(num)
            num = 0
            i = 0
            while i < len(strnum):
                num += int(strnum[i])
                i += 1

        return num

class Solution2:
    def addDigits(self, num: int) -> int:
        if num<10:return num
        if num % 9 ==0:return 9
        return num%9

class Solution3:
    #九进制
    def addDigits(self, num: int) -> int:
        if num==0:return num #与python的下取整有关
        return (num-1) % 9 + 1

k=Solution2()
print(k.addDigits(12))
