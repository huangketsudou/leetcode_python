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

        
        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0: return
        i = 0
        while i < n // 2:
            j = i
            while j < n - i - 1:

                cursorx, cursory = i, j
                currentnumber = matrix[cursorx][cursory]
                count = 0
                while count < 4:
                    print(cursorx, cursory)
                    nx, ny = cursory, n - 1 - cursorx
                    tmp = matrix[nx][ny]
                    matrix[nx][ny] = currentnumber
                    currentnumber = tmp
                    cursorx, cursory = nx, ny
                    count += 1
                j += 1
            i += 1


class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

k=Solution()
matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
k.rotate(matrix)
print(matrix)
