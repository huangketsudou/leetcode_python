from math import sqrt, floor
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return floor( sqrt(1/4+2*n)-1/2 )

