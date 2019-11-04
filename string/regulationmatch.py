from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #超时
        if len(s) < len(p) - p.count('*'): return False
        if not s and not p:return True
        if s and not p:return False
        if not s and p:
            if p!='*'*len(p):return False
            else:return True
        if p[0] == '*':
            j=0
            if j <len(p)-1 and p[j]==p[j+1]:
                j+=1
            return self.isMatch(s[1:],p[j:]) or self.isMatch(s,p[j+1:])
        if s[0]==p[0] or p[0]=='?':
            return self.isMatch(s[1:],p[1:])
        return False


class Solution2:  # 回溯
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0  # 用i索引s字符串，用j索引p字符串
        back_j = -1  # 记录p字符串中星号出现的位置
        match_i = 0  # 记录s字符串中从0到match_i位置都能匹配
        ls = len(s)
        lp = len(p)
        while i < ls:
            if j < lp and (s[i] == p[j] or p[j] == '?'):  # 若匹配，i和j往后移
                i += 1
                j += 1
            elif j < lp and p[j] == '*':  # *号出现，i不变，j记录
                back_j = j  # 记录星号的位置，方便回溯
                match_i = i  # 因为j处的'*'可以匹配s[i]，所以match_i = i
                j += 1  # i不变，j加1，看i能否和星号后面字符的匹配，若匹配则i和j后移，若不匹配则回溯
            elif back_j != -1:  # 回溯，j回到星号位置的下一个位置，i回到match_i的下一个位置
                j = back_j + 1
                match_i += 1  # match_i一直加1就是为了找到能和back_j的下一个位置匹配的，若匹配i和j各自加1继续往后移，
                # 若不匹配j继续回到back_j的下一个位置，match_i继续加1，直到match_i和back_j匹配，或者i溢出
                i = match_i
            else:  # 还没出现*,但s[i]和p[j]已经不匹配了，所以False
                return False
        return list(p[j:]).count('*') == len(p[j:])


class Solution3:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn = len(s)
        pn = len(p)
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True
        for j in range(1, pn + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if (s[i - 1] == p[j - 1] or p[j - 1] == "?"):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]



k=Solution3()
print(k.isMatch("bbaaababaaabaaaababaabbabababbbaabaababbbaabababbb",
"**b*aa*b***aa****b*aaaa*"))

