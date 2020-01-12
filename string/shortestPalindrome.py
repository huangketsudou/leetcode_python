from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        k = len(s)
        if k == 0: return ''
        while k > 0:
            if s[:k] == s[:k][::-1]:
                break
            k -= 1
        return s[k:][::-1] + s


class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        i, n = 0, len(s)
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == n: return s
        remain_rev = s[i:][::-1]
        print(remain_rev)
        return remain_rev + self.shortestPalindrome(s[:i]) + s[i:]



class Solution3:
    #KMP匹配算法
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        s_new=s+'#'+s[::-1]
        n_new=len(s_new)
        f=[0]*n_new
        for i in range(1,n_new):
            t=f[i-1]
            while t>0 and s_new[i]!=s_new[t]:
                t=f[t-1]
            if s_new[i]==s_new[t]:
                t+=1
            f[i]=t
        print(f)
        return s[::-1][:n-f[n_new-1]]+s



k = Solution3()
print(k.shortestPalindrome('acdbca'))
