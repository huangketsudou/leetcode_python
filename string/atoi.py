class Solution:
    def myAtoi(self, s: str) -> int:
        length=len(s)
        answer=0
        i=0
        negative=1
        Maxleft=2**31//10
        print('MAx'+str(Maxleft))
        while i<length:
            if s[i]=='+':
                i+=1
                break
            if s[i]=='-':
                negative=-1
                i+=1
                break
            if 48<=ord(s[i])<=57:
                break
            if s[i]==' ':
                i+=1
            else:
                return 0
        while i<length:
            k=ord(s[i])-48
            if 0<=k<=9:
                print(answer)
                if negative==1 and (answer>Maxleft or (answer==Maxleft and k>7)):
                    return 2**31-1
                if negative==-1 and (answer>Maxleft or (answer==Maxleft and k>8)):
                    return -2**31
                answer = answer * 10 + k
            else:
                break
            i+=1
        return answer*negative

k=Solution()
print(k.myAtoi("-2147483648"))
