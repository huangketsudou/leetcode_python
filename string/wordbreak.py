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


class Solution:
    #超时，改进方向，利用字符长度修改
    # @functools.lru_cache(None)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        queue = [0]
        answer = []
        ans = []
        n = len(s)
        while len(queue) != 0:
            start = queue.pop(0)
            if start == n:
                ans.append(answer.pop(0))
                continue
            tmp = [] if len(answer) == 0 else answer.pop(0)
            for i in range(start + 1, n + 1):
                if s[start:i] in wordDict:
                    queue.append(i)
                    answer.append(tmp + [s[start:i]])
        return list(map(lambda x: ' '.join(x), ans))


class Solution3:
    # 总想着O(n),关键是解决问题

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def __dfs(s, end, wordDict, res, path, dp):
            if s[:end + 1] in wordDict:
                path.appendleft(s[:end + 1])
                res.append(' '.join(path))
                path.popleft()

            for i in range(end):
                if dp[i]:
                    suffix = s[i + 1:end + 1]
                    if suffix in wordDict:
                        path.appendleft(suffix)
                        __dfs(s, i, wordDict, res, path, dp)
                        path.popleft()

        from collections import deque
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        dp.pop(0)
        res = []
        if dp[-1]:
            queue = deque()
            __dfs(s, n - 1, wordDict, res, queue, dp)

        return res


k = Solution3()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
g = k.wordBreak(s, wordDict)
print(g)

