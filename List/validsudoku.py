from typing import List

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[{} for i in range(9)]
        col=[{} for i in range(9)]
        box=[{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                cur=board[i][j]
                if cur=='.':
                    continue
                boxid=(i//3)*3+j//3*3
                if row[i].get(cur,0)!=0 or col[j].get(cur,0)!=0 or box[boxid].get(cur,0)!=0:
                    return False
                else:
                    row[i][cur]=1
                    col[j][cur]=1
                    box[boxid][cur]=1

        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[x for x in y if x != '.'] for y in board]
        col = [[x for x in y if x != '.'] for y in zip(*board)]
        pal = [[board[i + m][j + n] for m in range(3) for n in range(3) if board[i + m][j + n] != '.'] for i in
               (0, 3, 6) for j in (0, 3, 6)]
        return all(len(set(x)) == len(x) for x in (*row, *col, *pal))
