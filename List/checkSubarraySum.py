from typing import List
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        number = defaultdict(int)
        number[0] = -1
        consum = 0
        for i, v in enumerate(nums):
            consum += v
            if k != 0:  # 当k为0时保留原值，因为只有0才是0的倍数
                consum %= k
            if consum in number:
                if i - number[consum] > 1:
                    return True
            else:
                number[consum] = i
        return False
