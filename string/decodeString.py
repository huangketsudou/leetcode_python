from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        i = 0
        ans = ''
        count = ''
        while i < n:
            if s[i].isdigit():
                count += s[i]
            elif s[i] == '[':
                lv = 1
                j = i
                while lv:
                    j += 1
                    if s[j] == '[':
                        lv += 1
                    elif s[j] == ']':
                        lv -= 1
                ans += int(count) * self.decodeString(s[i + 1:j])
                count=''
                i = j
            else:
                ans += s[i]
            i += 1
        return ans

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res



k=Solution()
print(k.decodeString("2[abc]3[cd]ef"))