class Solution(object):
    def isToeplitzMatrix(self, matrix):
        n, m = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i == 0 or j == 0:
                    continue
                else:
                    if val != matrix[i - 1][j - 1]:
                        return False
        return True
