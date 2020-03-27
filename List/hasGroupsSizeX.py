#数组的最大公约数

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        c=Counter(deck)
        number=list(set(c.values()))
        number.sort()
        for i in range(min(number),1,-1):
            flag=True
            for j in number:
                if j % i!=0:
                    flag=False
            if flag:return True
        return False


class Solution(object):
    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2



k=Solution()
print(k.hasGroupsSizeX([1]))
