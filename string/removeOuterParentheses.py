class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        i = 0
        ans = []
        tmp = ''
        count = 0
        while i < len(S):
            if S[i] == '(':
                count += 1
            else:
                count -= 1
            tmp += S[i]
            if count == 0:
                ans.append(tmp)
                tmp = ''
            i += 1
        return ''.join(map(lambda x: x[1:-1], ans))
