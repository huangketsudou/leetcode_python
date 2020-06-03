import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.arr = w
        prev = 0
        self.consum = []
        for i in range(len(w)):
            prev += w[i]
            self.consum.append(prev)
        self.summary = prev

    def pickIndex(self) -> int:
        number = random.randint(1, self.summary)
        idx = bisect.bisect_left(self.consum, number)
        return self.arr[idx]

