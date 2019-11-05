from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        record={}
        for i in range(n):
            for j in range(n):
                if (n-1-j,i) in record:
                    record[(i, j)] = matrix[i][j]
                    matrix[i][j]=record[(n-1-j,i)]
                    del record[(n-1-j,i)]
                else:
                    record[(i,j)]=matrix[i][j]
                    matrix[i][j]=matrix[n-1-j][i]
        del record


k=Solution()
matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
k.rotate(matrix)
print(matrix)
