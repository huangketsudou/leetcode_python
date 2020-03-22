class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:


        A.sort()
        n=len(A)
        if n<2:return 0
        res=0
        for i in range(1,n):
            while A[i]<=A[i-1]:
                res+=1
                A[i]+=1
        return res


class Solution2:
    def minIncrementForUnique(self, A: List[int]) -> int:



        def findpos(a):
            b=pos[a]
            if b==-1:
                pos[a]=a
                return a
            b=findpos(b+1)
            pos[a]=b
            return b

        pos=[-1]*80000
        move=0

        for a in A:
            b=findpos(a)
            move+=b-a

        return move


k=Solution2()
print(k.minIncrementForUnique([1,1,1,1,1]))
