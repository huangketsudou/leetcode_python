class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n,m=len(A),len(A[0])
        pivot=[True]*m
        for i in range(m):
            for j in range(1,n):
                if ord(A[j][i])<ord(A[j-1][i]):
                    pivot[i]=False
                    break
        return m-sum(pivot)

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        return len([1 for col in zip(*A) if sorted(col)!=list(col)])

k=Solution()
print(k.minDeletionSize(["zyx", "wvu", "tsr"]))
