class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:return -1
        return max(len(a),len(b))
        
        
        
        
 class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len,reverse=True)
        n=len(strs)
        for i in range(n):
            flag=True
            for j in range(n):
                if i==j:
                    continue
                if len(strs[i])>len(strs[j]):
                    break
                if self.issubsequence(strs[i],strs[j]):
                    flag=False
                    break
            if flag:
                return len(strs[i])
        return -1


    def issubsequence(self,a,b):
        j=0
        for i in b:
           if j<len(a) and a[j]==i:
               j+=1
        return j==len(a)
