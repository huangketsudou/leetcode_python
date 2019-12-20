from typing import List
import functools


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #思路要固定一个点进行统计
        from collections import defaultdict,Counter
        points_dict=Counter(tuple(point) for point in points)
        not_repeat_points=list(points_dict.keys())
        n=len(not_repeat_points)
        if n==1:return points_dict[not_repeat_points[0]]
        res=0
        def gcd(x,y):
            if y==0:
                return x
            return gcd(y,x%y)

        for i in range(n-1):
            x1,y1=not_repeat_points[i][0],not_repeat_points[i][1]
            slope=defaultdict(int)
            for j in range(i+1,n):
                x2,y2=not_repeat_points[j][0],not_repeat_points[j][1]
                dy,dx=y2-y1,x2-x1
                g=gcd(dy,dx)
                if g!=0:
                    dy//=g
                    dx//=g
                slope['{}/{}'.format(dy,dx)]+=points_dict[not_repeat_points[j]]
            print(slope)
            res=max(res,max(slope.values())+points_dict[not_repeat_points[i]])
        return res



k=Solution()
print(k.maxPoints([[1,1],[2,2],[3,3]]))
