from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.size = len(nums)

    def pick(self, target: int) -> int:
        i = 0
        count = 0
        reserve = 0
        while i < self.size:
            if self.array[i] == target:
                count += 1
                rand = random.randint(1, count)
                if rand == count:
                    reserve = i
            i += 1
        return reserve
