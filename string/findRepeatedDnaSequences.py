from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L,n=10,len(s)
        seen,ans=set(),set()
        for start in range(n-L+1):
            tmp=s[start:start+L]
            if tmp in seen:
                ans.add(tmp)
            seen.add(tmp)
        return list(ans)


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L,n=10,len(s)
        if n<L:return []
        a=4
        aL=pow(a,L)
        to_int={'A':0,"C":1,"G":2,"T":3}
        nums=[to_int.get(s[i]) for i in range(n)]
        h=0
        seen,ans=set(),set()
        for start in range(n-L+1):
            if start!=0:
                h=h*a-nums[start-1]*aL+nums[start+L-1]
            else:
                for i in range(L):
                    h=h*a+nums[i]
            if h in seen:
                ans.add(s[start:start+L])
            seen.add(h)
        return list(ans)


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L,n=10,len(s)
        if n<=L:return []
        to_int={'A':0,"C":1,"G":2,"T":3}
        nums=[to_int.get(s[i]) for i in range(n)]
        bitmask=0
        seen,ans=set(),set()
        for start in range(n-L+1):
            if start!=0:
                bitmask<<=2
                bitmask|=nums[start+L-1]
                bitmask&=~(3<<2*L)
            else:
                for i in range(L):
                    bitmask<<=2
                    bitmask|=nums[i]
            if bitmask in seen:
                ans.add(s[start:start+L])
            seen.add(bitmask)
        return list(ans)
