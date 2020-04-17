from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return
        self.matrix = matrix
        row, col = len(matrix), len(matrix[0])
        self.cumsummatrix = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.cumsummatrix[i][j] = self.cumsummatrix[i][j - 1] + matrix[i - 1][j - 1]
        for j in range(1, col + 1):
            for i in range(1, row + 1):
                self.cumsummatrix[i][j] += self.cumsummatrix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cumsummatrix[row2+1][col2+1] - self.cumsummatrix[row1][col2 + 1] - self.cumsummatrix[row2 + 1][col1] + \
               self.cumsummatrix[row1][col1]
