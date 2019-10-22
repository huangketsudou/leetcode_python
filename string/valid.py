class Solution:
    def isValid(self, s: str) -> bool:
        match=['()','{}','[]']
        tmp=''
        for i in s:
            tmp+=i
            if len(tmp)<2:
                continue
            if tmp[-2:] in match:
                tmp=tmp[:-2]
        if tmp:
            return False
        return True


class Solution2:
    def isValid(self, s: str) -> bool:
        n = len(s)
        # if n < 1:
        #     return True
        dicts = {'}':'{',']':'[',')':'('}
        stack = []
        for i in range(n):
            if s[i] in dicts:
                if not stack or stack[-1] != dicts[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        if stack:
            return False
        return True

k=Solution2()
print(k.isValid(''))
