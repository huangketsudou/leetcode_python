from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m==0:return []
        n = len(matrix[0])
        boudary = min(m, n)
        answer = []
        k = 0
        while k < (boudary + 1) // 2:
            i = j = k
            while j < n - k:
                answer.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            while i < m - k:
                answer.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            while j >= k and i>k:
                answer.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            while i > k and j<n-k-1:
                answer.append(matrix[i][j])
                i -= 1
            k += 1
        return answer


k = Solution()
matrix = [
 [2,5,8],
 [4,0,-1]
]
print(k.spiralOrder(matrix))
