class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        p1 = p2 = 0
        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                p2 += 1
                p1 += 1
                res += 1
            else:
                p2 += 1
        return res


k = Solution()
print(k.findContentChildren([12, 3, 4], [1, 2, 3]))
