from collections import Counter
from itertools import combinations, product


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        res=0
        for v in c.values():
            res+=v//2*2
            if res %2==0 and v%2==1:
                res+=1
        return res

k=Solution()
