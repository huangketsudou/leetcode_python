from typing import List


class Solution:
    # 总想着O(n),关键是解决问题
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


class Solution2:
    # 总想着O(n),关键是解决问题
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue=[0]
        n=len(s)
        visited=[0]*n
        while len(queue)!=0:
            start=queue.pop(0)
            if visited[start]==0:
                for i in range(start+1,n+1):
                    if s[start:i] in wordDict:
                        queue.append(i)
                        if i==n:
                            return True
                visited[start]=1
        return False


k=Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(k.wordBreak(s,wordDict))

