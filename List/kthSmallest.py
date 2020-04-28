from typing import List
import heapq
import bisect


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        Ksmall = []
        for i in range(row):
            for j in range(col):
                heapq.heappush(Ksmall, matrix[i][j])
                if len(Ksmall) > k:
                    heapq.heappop(Ksmall)
        return Ksmall[0]


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        row, col = len(matrix), len(matrix[0])
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for i in range(row):
                count += bisect.bisect_right(matrix[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            count = self.search(matrix, mid, row, col)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def search(self, array, target, row, col):
        i = row - 1
        j = 0
        res = 0
        while i >= 0 and j < col:
            if array[i][j] <= target:
                res += i + 1
                j += 1
            else:
                i -= 1
        return res
