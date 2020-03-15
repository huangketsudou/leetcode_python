class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)





        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col


        F={25:25}


        def my_find(x):
            F.setdefault(x,x)
            if F[x]!=x:
                F[x]=my_find(F[x])
            return F[x]


        def my_union(x,y):
            x1=my_find(x)
            y1=my_find(y)
            if x1!=y1:
                F[x1]=y1

        #my_union必须配合my_find使用



        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        my_union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                my_union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if my_find(dummy) == my_find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
