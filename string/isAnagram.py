class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        sc=Counter(s)
        tc=Counter(t)
        return tc==sc
