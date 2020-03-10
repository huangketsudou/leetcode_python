class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        start=0
        for i in s:
            tmp=t.find(i,start)
            if tmp==-1:
                return False
            start=tmp+1
        return True


class Solution(object):
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)


class Solution(object):
    def isSubsequence(self, s, t):

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False




k=Solution()
print(k.isSubsequence(s = "", t = "1"))
