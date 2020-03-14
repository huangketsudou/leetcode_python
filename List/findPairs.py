class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return len(set([i for i in nums if nums.count(i) >= 2]))
        cl = [i + k for i in nums]
        return len(set(cl) & set(nums))

class Solution2:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:return 0
        if k==0:return len(set([i for i in nums if nums.count(i)>1]))
        g=list(set(nums))
        g.sort()
        n=len(g)
        i=j=0
        res=0
        while i<n and j<n:

            if g[i]+k==g[j]:
                res+=1
                i+=1
                j+=1
            elif g[i]+k<g[j]:
                i+=1
            else:
                j+=1
        return res



k=Solution2()
print(k.findPairs([1,1,1,1,1,1],0))
