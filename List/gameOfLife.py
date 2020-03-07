class Solution:
#奇偶数字标记数字位是否改变，如果变更后数字还是活着的，那么变更为3，死数字复活变更为2，活数字死了不变更
#这样通过 board[i][j] & 1可以判断原来数字的状态，board[i][j]>>1 可以变更数字状态
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                lives = self.countaliveneighbor(board, i, j, n, m)
                if board[i][j]==0 and lives == 3:
                    board[i][j] = 2
                if board[i][j]==1 and lives in {2, 3}:#这里不要用 board[i][j]作为条件，因为2也是True
                    board[i][j] = 3

        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1

    def countaliveneighbor(self, board, x, y, n, m):
        dict = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        count = 0
        for i, j in dict:
            nbx, nby = x + i, y + j
            if 0 <= nbx < n and 0 <= nby < m:
                count += (board[nbx][nby] & 1)
        return count


k = Solution()
b = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
# print(k.gameOfLife(b))
# print(b)

