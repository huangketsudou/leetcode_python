class Solution:
#老实人解法
    def checkRecord(self, s: str) -> bool:
        A=0
        L=0
        i=0
        n=len(s)
        while i<n:
            if s[i]=='A':
                A+=1
            elif s[i]=='L':
                if i==0 or s[i-1]!='L':
                    L=1
                else:
                    L+=1
            if A>1 or L>2:
                return False
            i+=1
        return True
        
        
        
        
class Solution:
    def checkRecord(self, s: str) -> bool:

        return not(len(s.split('A'))>2 or "LLL" in s)
