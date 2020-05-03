from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        MAX=max(candies)
        n=len(candies)
        ans=[False]*n
        for i in range(n):
            if candies[i]+extraCandies>=MAX:
                ans[i]=True
        return ans