from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = len(A)
        ans = [False] * n
        tmp=0
        for i,v in enumerate(A):
            tmp=(2*tmp+v)%5
            if tmp==0:
                ans[i]=True
        return ans