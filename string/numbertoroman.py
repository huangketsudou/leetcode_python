class Solution2:
    def intToRoman(self,num):
        T=''
        H=''
        D=''
        last=''
        if num>=1000:
            thousand=num//1000
            num%=1000
            T='M'*thousand
        if num>=100:
            hundred=num//100
            num%=100
            if hundred==9:
                H='CM'
            elif hundred==4:
                H='CD'
            elif hundred>=5:
                H='D'+'C'*(hundred-5)
            else:
                H='C'*hundred
        if num>=10:
            ten=num//10
            num%=10
            if ten==9:
                D='XC'
            elif ten==4:
                D='XL'
            elif ten>=5:
                D='L'+'X'*(ten-5)
            else:
                D='X'*ten
        if num==9:
            last='IX'
        elif num==4:
            last='IV'
        elif num>=5:
            last='V'+'I'*(num-5)
        else:
            last='I'*num
        return T+H+D+last

class Solution:
    def intToRoman(self, num: int) -> str:
        sign=((1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),
              (90,'XC'),(50,'L'),(40,'XL'),(10,'X'),
              (9,'IX'),(5,'V'),(4,'IV'),(1,'I'))
        answer=''
        for i,c in sign:
            if num>=i:
                answer+=c*(num//i)
                num%=i
        return answer


k=Solution()
print(k.intToRoman(1994))
