from typing import List
from collections import defaultdict


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        kinds = {1, 2, 3, 4}
        road = defaultdict(list)
        for start, end in paths:
            road[start].append(end)
            road[end].append(start)
        gardenflower={}
        result=[]
        for i in range(1,N+1):
            if i in road:
                used_flower=[]
                for connected_garden in road[i]:
                    if connected_garden in gardenflower:
                        used_flower.append(gardenflower[connected_garden])
                this_garden_flower=(kinds-set(used_flower)).pop()
            else:
                this_garden_flower=1
            result.append(this_garden_flower)
            gardenflower[i]=this_garden_flower
        return result