#出现了很多次



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
