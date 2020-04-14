class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(('1'*len(bin(N)[2:])),2)-N



class Solution2:
    def bitwiseComplement(self, N: int) -> int:
        if N==0:return 1
        tmp=1
        while tmp<=N:
            tmp<<=1
        return tmp-1-N

k=Solution2()
print(k.bitwiseComplement(1))


class Solution2:
    def bitwiseComplement(self, N: int) -> int:
        if N==0:return 1
        tmp1=1
        tmp2=N
        while tmp2>0:
            N ^= tmp1
            tmp1<<=1
            tmp2>>=1
        return N