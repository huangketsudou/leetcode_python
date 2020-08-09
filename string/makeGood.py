class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        i = 0
        while i<len(s):
            if not stack:
                stack.append(s[i])
            elif abs(ord(stack[-1])-ord(s[i]))==32:
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        return ''.join(stack)


k=Solution()
print(k.makeGood("leEeetcode"))