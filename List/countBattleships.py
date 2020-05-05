from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        row, col = len(board), len(board[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    ans += 1
                    if i > 0 and board[i - 1][j] == 'X':
                        ans -= 1

                    if j > 0 and board[i][j - 1] == 'X':
                        ans -= 1
        return ans

