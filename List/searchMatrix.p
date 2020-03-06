from typing import List
from collections import deque
import heapq


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:return False
        n,m=len(matrix),len(matrix[0])
        start_i,start_j=0,m-1

        while start_i<n and start_j>=0:
            if matrix[start_i][start_j]==target:
                return True
            elif matrix[start_i][start_j]>target:
                start_j-=1
            else:
                start_i+=1
        return False


k=Solution()
a=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(k.searchMatrix(a,6))

