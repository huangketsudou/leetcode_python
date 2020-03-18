class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        a = x1 < x3 < x2 < x4 and (y3 < y1 < y4 < y2 or y1 < y3 < y2 < y4)
        b = x3 < x1 < x4 < x2 and (y3 < y1 < y4 < y2 or y1 < y3 < y2 < y4)

        return a or b


class Solution2:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        return not (y1 >= y4 or y2 <= y3 or x1 >= x4 or x3 >= x2)

class Solution(object):
    #思路，重叠的部分中心也是一个矩形
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))




k = Solution2()
print(k.isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]))
