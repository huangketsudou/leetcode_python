from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    # 寻找边长，要从靠近i侧找起，寻找较小值
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, pow(min(width, i - k + 1), 2))
        return maxarea


class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        if m==0 : return 0
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        maxlength=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                maxlength=max(dp[i][j],maxlength)
        return maxlength*maxlength


class Solution3:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        if m==0:return 0
        n=len(matrix[0])
        dp=[0]*(n+1)
        maxlength=0
        prevlength=0
        for i in range(m):
            for j in range(n):
                tmp=dp[j+1]
                if matrix[i][j]=='1':
                    dp[j+1]=min(dp[j],dp[j+1],prevlength)+1
                    maxlength = max(maxlength, dp[j+1])
                else:
                    dp[j+1]=0
                prevlength=tmp
        return maxlength**2


class Solution4:
    #把二维问题变为一维问题
    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                length = min(heights[stack.pop()], (i - stack[-1] - 1))
                maxarea = max(maxarea, length**2)
            stack.append(i)

        while stack[-1] != -1:
            length=min(heights[stack.pop()],(len(heights)-stack[-1]-1))
            maxarea = max(maxarea, length**2)
        return maxarea


    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix: return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones

                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update maxarea with the maximum area from this row's histogram
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea


a=[["1","0"],["1","0"]]
b = [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]]
c=[["1"],["0"],["1"],["1"],["1"],["1"],["0"]]

d=[["1","1"],["1","1"]]
k=Solution4()
print(k.maximalSquare(d))
