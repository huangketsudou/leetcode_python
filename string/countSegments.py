class Solution:
    def countSegments(self, s: str) -> int:
        if not s:return 0
        i=0
        res=0
        while i<len(s):

            if s[i]==' ':
                i+=1
                continue
            while i<len(s) and s[i]!=' ':
                i+=1
            res+=1
        return res
