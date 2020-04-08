class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maximun=max(A)
        minimum=min(A)
        if minimum+K>=maximun-K:
            return 0
        else:
            return maximun-minimum-2*K
