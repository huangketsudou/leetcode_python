class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        i = n - 1
        carry = 0
        count = 0
        while i >= 0:
            if i==0:
                if carry:
                    count+=1
            elif s[i] == '1' and carry == 0:
                carry = 1
                count += 2
            elif s[i] == '1' and carry == 1:
                count += 1
            elif s[i] == '0' and carry == 1:
                carry = 1
                count += 2
            else:
                count += 1
            i -= 1
        return count
        
        
class Solution:
    def numSteps(self, s: str) -> int:
        number=int(s,base=2)
        count=0
        while number>1:
            if number % 2==1:
                number+=1
                count+=1
            number//=2
            count+=1
        return count
