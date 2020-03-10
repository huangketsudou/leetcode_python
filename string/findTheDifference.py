class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl,tl=list(s),list(t)
        sl.sort();tl.sort()
        for i in range(len(s)):
            if sl[i]!=tl[i]:
                return tl[i]

        return tl[-1]

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)
        for i in range(ord("a"), ord("z") + 1):
            tmp = chr(i)
            if c2[tmp] - c1[tmp] == 1:
                return tmp

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tmp = s + t
        res = ord(tmp[0])
        for t in tmp[1:]:
            res ^= ord(t)
        return chr(res)

from functools import reduce
import operator
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(operator.xor, map(ord, s + t)))




k=Solution()
print(k.findTheDifference(s = "abcd",t = "abcde"))
