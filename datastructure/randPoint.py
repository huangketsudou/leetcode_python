from typing import List
import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = self.x - self.radius + random.random() * 2 * self.radius
            y = self.y - self.radius + random.random() * 2 * self.radius
            if (x - self.x) ** 2 + (y - self.y) ** 2 <=self.radius**2:
                return [x,y]
