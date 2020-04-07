class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        B.sort()
        n,m=len(A),len(B)
        i=j=0
        target=(sum(A)+sum(B))//2-sum(A)
        while i<n and j<m:
            print(i,j)
            if target<-A[i]+B[j]:
                i+=1
            elif target>-A[i]+B[j]:
                j+=1
            else:
                return [A[i],B[j]]

        return [-1,-1]


class Solution(object):
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]


k=Solution()
print(k.fairCandySwap([2],[1,3]))
