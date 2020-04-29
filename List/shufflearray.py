from typing import List
from random import choice
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        for i,v in enumerate(self.origin):
            self.nums[i]=v
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        i = n
        while i > 0:
            idx = choice(range(i))
            self.nums[idx], self.nums[i - 1] = self.nums[i - 1], self.nums[idx]
            i -= 1
        return self.nums


class Solution2:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array




a=[1,2,3,4,5,6,7,8]
k=Solution2(a)
k.shuffle()
print(a)
k.shuffle()
print(a)
k.shuffle()
print(a)
k.reset()
print(a)

