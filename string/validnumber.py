from typing import List


class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip(' ')
        evalid=True
        dotvalid=True
        n=len(s)
        if n==0:return False
        for i in range(n):
            if i==0 and s[i]=='e':return False
            if evalid and s[i]=='e':
                if i==n-1:return False
                if s[i-1] not in '0123456789.':return False
                evalid=False
                dotvalid=False
            elif dotvalid and s[i]=='.':
                if (i==n-1 and s[i-1] not in '0123456789') or (i==0 and s[i+1] not in '0123456789'):return False
                dotvalid=False
            elif s[i] in '+-' and (i == 0 or s[i - 1] in 'Ee') and i<n-1:
                continue
            elif s[i] not  in '0123456789':
                return False
        return True

k=Solution()
print(k.isNumber('-e3'))

