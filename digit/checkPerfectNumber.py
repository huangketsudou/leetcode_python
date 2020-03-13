class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        p=[1]
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                p.append(i)
                p.append(num//i)
        return sum(p)==num




k=Solution()
print(k.checkPerfectNumber(0))
