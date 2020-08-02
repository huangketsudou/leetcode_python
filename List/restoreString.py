from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        l = [0] * n
        for c, i in zip(s, indices):
            l[i] = c
        return "".join(l)


k = Solution()
print(k.restoreString(s="art", indices=[1, 0, 2]))
