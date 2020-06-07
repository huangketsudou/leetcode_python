from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        length = len(arr)
        m = arr[(length - 1) // 2]
        arr.sort(key=lambda x:(abs(x-m),x),reverse=True)
        return arr[:k]