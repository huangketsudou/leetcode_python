from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        #print(dp)
        return dp[-1][-1]


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1

        return helper(0, 0)


class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1),len(word2))
        stack=[(0,0,0)]
        mem=set()
        while stack:
            newstack=[]
            while stack:
                i,j,lv=stack.pop()
                if (i,j) in mem:
                    continue
                else:
                    mem.add((i,j))
                if i==len(word1) and j==len(word2):
                    return lv
                if i<len(word1) and j<len(word2):
                    if word1[i]==word2[j]:
                        stack.append((i+1,j+1,lv))
                        continue
                    else:
                        #rep
                        newstack.append((i+1,j+1,lv+1))
                #add
                if j<len(word2):
                    newstack.append((i,j+1,lv+1))
                #del
                if i<len(word1):
                    newstack.append((i+1,j,lv+1))
            stack=newstack


k=Solution()
print(k.minDistance('horse','ros'))
