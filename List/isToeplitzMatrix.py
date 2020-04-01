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

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
