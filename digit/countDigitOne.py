class Solution:
    def countDigitOne(self, n: int) -> int:
        import math
        if n<1:
            return 0       
        r = 0
        while n>=10:
            m = int(math.log10(n))
            r += n - 10**m+10**(m-1)*m+1 if n/10**m <2 else 10**m+10**(m-1)*m*(n//10**m)
            n-= 10**m*(n//10**m)
        return int(r+1) if n>0 else int(r)
 class Solution:
    def countDigitOne(self, n: int) -> int:
        if n<0:return 0
        strnumber=str(n)
        return self.conntDigitOneStr(strnumber)

    def conntDigitOneStr(self,strn):

        first=int(strn[0])
        length=len(strn)

        if length==1 and first==0:
            return 0
        if length==1 and first>0:
            return 1
        numberfirstDigit=0
        if first>1:
            numberfirstDigit = pow(10, length - 1)
        elif first==1:
            numberfirstDigit = int(strn[1:])+1

        numberOtherDigit=first*pow(10,length-2)*(length-1)
        numberRecursive=self.conntDigitOneStr(strn[1:])
        return numberfirstDigit+numberOtherDigit+numberRecursive



k=Solution()
print(k.countDigitOne(23))
