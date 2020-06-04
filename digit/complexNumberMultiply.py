class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        ra, va = a.split('+')
        rb, vb = b.split('+')
        ra, va = int(ra), int(va[:-1])
        rb, vb = int(rb), int(vb[:-1])
        return str(ra*rb - va*vb)+'+'+str(va*rb+ra*vb)+'i'