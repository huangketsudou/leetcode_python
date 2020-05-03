from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        degree = defaultdict(int)
        for start, end in paths:
            degree[start] += 1
            degree[end] = degree[end]
        for k,v in degree.items():
            if v==0:
                return k
        return ''