from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isleaf(grid, row, col):
            return all(grid[i][j] == grid[0][0] for i in range(row) for j in range(col))

        def dfs(matrix):
            row = len(matrix)
            col = len(matrix[0])
            if isleaf(matrix, row, col):
                return Node(True if grid[0][0] else False, True, None, None, None, None)
            else:
                return Node('*', False, dfs([row[:len(matrix) // 2] for row in grid[:len(matrix) // 2]]),
                            dfs([row[len(matrix) // 2:] for row in grid[:len(matrix) // 2]]),
                            dfs([row[:len(matrix) // 2] for row in grid[len(matrix) // 2:]]),
                            dfs([row[len(matrix) // 2:] for row in grid[len(matrix) // 2:]]))

        return dfs(grid)
