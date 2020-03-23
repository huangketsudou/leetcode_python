class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        k = len(ops)
        if not k: return m*n
        res_x, res_y = ops[0]
        for i in range(1, k):
            res_x = min(res_x, ops[i][0])
            res_y = min(res_y, ops[i][1])
        return res_x*res_y
