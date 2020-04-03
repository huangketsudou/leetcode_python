class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        index=[]
        for i,c in enumerate(S):
            if c==C:
                index.append(i)
        n=len(S)
        result=[n]*n
        for i in range(n):
            for j in index:
                result[i]=min(result[i],abs(i-j))
        return result

class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans



k=Solution()
print(k.shortestToChar(S = "loveleetcode", C = 'e'))
