import random


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.nc = n_cols
        self.nr = n_rows
        self.rem = n_rows * n_cols
        self.mapping = dict()

    def flip(self) -> List[int]:
        r = random.randint(0, self.rem -1)
        self.rem -= 1
        x = self.mapping.get(r, r)
        self.mapping[r] = self.mapping.get(self.rem, self.rem)
        return [x // self.nc, x % self.nc]

    def reset(self) -> None:
        self.mapping.clear()
        self.rem = self.nc * self.nr
