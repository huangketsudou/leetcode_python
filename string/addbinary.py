from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer=''
        m=len(a)
        n=len(b)
        carry=0
        reversedA=a[::-1]
        reversedB=b[::-1]
        i=0
        while i<max(m,n):
            d_a=int(reversedA[i]) if i < m else 0
            d_b=int(reversedB[i]) if i < n else 0
            digit_sum=d_a+d_b+carry
            if digit_sum<2:
                answer=str(digit_sum)+answer
                carry=0
            else:
                answer=str(digit_sum-2)+answer
                carry=1
            i+=1
        if carry:answer='1'+answer
        return answer


k=Solution()
print(k.addBinary('1111','1111'))
