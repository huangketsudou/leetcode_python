class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s==p:
            return True
        if not p and s:
            return False
        if len(p)>1 and p[1]=='*':
            if len(s)!=0 and(p[0]==s[0] or p[0]=='.'):
                return self.isMatch(s[1:],p)  or self.isMatch(s,p[2:])
            else:
                return self.isMatch(s,p[2:])
        else:
            if s and (p[0]==s[0] or p[0]=='.'):
                return self.isMatch(s[1:],p[1:])
        return False
        #time limit exceed
        
        
        
        
        
class Solution2(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


class Solution3(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True#标记均为两序列末尾这种情况为TRUE
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                #搜索是否pattern里有符合s*这种模式的，末尾可以匹配这种情况
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        print(dp)
        return dp[0][0]


class Solution4(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
