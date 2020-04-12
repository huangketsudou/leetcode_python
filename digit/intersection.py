class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:

        def inside(x1, y1, x2, y2, xk, yk):
            return (x1 == x2 or min(x1, x2) <= xk <= max(x1, x2)) and (y1 == y2 or min(y1, y2) <= yk <= max(y1, y2))

        def update(ans, x, y):
            return [x, y] if not ans or [x, y] < ans else ans

        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2
        ans = list()
        if (x4 - x3) * (y2 - y1) == (x2 - x1) * (y4 - y3):
            if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                if inside(x1, y1, x2, y2, x3, y3):
                    ans = update(ans, x3, y3)
                if inside(x1, y1, x2, y2, x4, y4):
                    ans = update(ans, x4, y4)
                if inside(x3, y3, x4, y4, x1, y1):
                    ans = update(ans, x1, y1)
                if inside(x3, y3, x4, y4, x2, y2):
                    ans = update(ans, x2, y2)
        else:
            t1 = (x3 * (y4 - y3) + y1 * (x4 - x3) - y3 * (x4 - x3) - x1 * (y4 - y3)) / (
                    (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = (x1 * (y2 - y1) + y3 * (x2 - x1) - y1 * (x2 - x1) - x3 * (y2 - y1)) / (
                    (x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3))
            if 0.0 <= t1 <= 1.0 and 0.0 <= t2 <= 1.0:
                ans = [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]
        return ans


class Solution:
    def intersection(self, start1, end1, start2, end2):
        #https://leetcode-cn.com/problems/intersection-lcci/solution/wo-jue-de-wo-yi-jing-hen-nu-li-liao-ke-yi-jiao-zhu/
        #大学线性代数
        x1, y1, x2, y2, x3, y3, x4, y4 = *start1, *end1, *start2, *end2
        det = lambda a, b, c, d: a * d - b * c
        d = det(x1 - x2, x4 - x3, y1 - y2, y4 - y3)
        p = det(x4 - x2, x4 - x3, y4 - y2, y4 - y3)
        q = det(x1 - x2, x4 - x2, y1 - y2, y4 - y2)
        if d != 0:
            lam, eta = p / d, q / d
            if not (0 <= lam <= 1 and 0 <= eta <= 1): return []
            return [lam * x1 + (1 - lam) * x2, lam * y1 + (1 - lam) * y2]
        if p != 0 or q != 0: return []
        t1, t2 = sorted([start1, end1]), sorted([start2, end2])
        if t1[1] < t2[0] or t2[1] < t1[0]: return []
        return max(t1[0], t2[0])
