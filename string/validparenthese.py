from typing import List



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n<2:
            return 0
        a=[-1]
        result=0
        for i in range(n):
            if s[i]=='(':
                a.append(i)
            else:
                a.pop(-1)
                if len(a)==0:
                    a.append(i)
                else:
                    result=max(result,i-a[-1])
        return result


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n<2:
            return 0
        i=left=right=maxlength=0
        while i<n:
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if right==left:
                maxlength=max(2*right,maxlength)
            elif right>left:
                right=left=0
            i+=1
        left=right=0
        j=n-1
        while j>=0:
            if s[j]==')':
                right+=1
            else:
                left+=1
            if right==left:
                maxlength=max(2*left,maxlength)
            elif right<left:
                left=right=0
            j-=1
        return maxlength


class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n<2:
            return 0
        dp=[0]*n
        result=0
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2 if i>=2 else 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    tmp=dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0
                    dp[i]=dp[i-1]+tmp+2
            result=max(result,dp[i])
        return result

k=Solution3()
print(k.longestValidParentheses('()))((()())'))
