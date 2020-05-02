from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        if not length:
            return 0
        fail={}
        MAX=0
        k=0
        for i in range(length):
            if  s[i] in fail:
                k=max(fail[s[i]],k)#k决定左边是哪里，当有fail[s[i]]<k时，就证明这些字母已经被删掉了
            MAX=max(MAX,i-k+1)
            fail[s[i]]=i+1
        return MAX

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        meet=set()
        stack=deque()
        ans=0
        for c in s:
            if c in meet:
                while c in meet:
                    top=stack.popleft()
                    meet.remove(top)
            meet.add(c)
            stack.append(c)
            ans=max(ans,len(stack))
        return ans


c=Solution()
print(c.lengthOfLongestSubstring('abba'))
