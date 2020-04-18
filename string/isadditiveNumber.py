
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        if n<3:return False

        for i in range(n//2+1):
            n1=num[:i+1]
            if len(n1)!=len(str(int(n1))):return False
            for j in range(i+1,n//2+i+1):
                n2=num[i+1:j+1]
                if len(n2)!=len(str(int(n2))):
                    break
                n3=num[j+1:]
                if self.isvalid(n1,n2,n3) and n3:
                    return True
        return False



    def isvalid(self,n1,n2,n3):
        while n3:
            t=str(int(n1)+int(n2))
            if n3.startswith(t):
                n1=n2;n2=t
                n3=n3[len(t):]
            else:
                return False
        return True