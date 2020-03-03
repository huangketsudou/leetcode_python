from typing import List


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        x=[A,C,E,G]
        y=[B,D,F,H]
        x.sort()
        y.sort()
        width1=C-A
        height1=D-B
        width2=G-E
        height2=H-F
        coverheight=height1+height2-(y[-1]-y[0]) if y[-1]-y[0]<height1+height2 else 0
        coverwidth=width1+width2-(x[-1]-x[0]) if x[-1]-x[0]<width1+width2 else 0

        return width1*height1+width2*height2-coverheight*coverwidth



class Solution2:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # 调整两个矩形位置, 让第一个矩形靠最左边
        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)
        # 没有重叠的情况
        if B >= H or D <= F or C <= E:
            return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
        # 重叠情况
        # 下边界
        down = max(A, E)
        # 上
        up = min(C, G)
        # 左
        left = max(B, F)
        # 右
        right = min(D, H)
        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - abs(up - down) * abs(left - right)



k=Solution()
print(k.computeArea(-2,0,0,1,-4,0,0,2))
