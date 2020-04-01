class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        for i, c in enumerate(seq):
            res.append((i&1)^(c=='('))
        return res

class Solution2:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans

