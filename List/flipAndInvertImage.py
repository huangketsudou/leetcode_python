class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        for i in range(n):
            start, end = 0, m - 1
            while start < end:
                A[i][start], A[i][end] = A[i][end], A[i][start]
                start += 1
                end -= 1
            for j in range(m):
                A[i][j] = 1 - A[i][j]
        return A


k = Solution()
print(k.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
