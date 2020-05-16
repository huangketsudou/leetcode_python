class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        hashmap=[0]*26
        hashmap[ord(p[0])-ord("a")]=1
        prelen=1
        for i in range(1,len(p)):
            gap=ord(p[i])-ord(p[i-1])
            if gap==1 or gap==-25:
                prelen+=1
            else:
                prelen=1
            hashmap[ord(p[i])-ord("a")]=max(hashmap[ord(p[i])-ord("a")],prelen)
        return sum(hashmap)


