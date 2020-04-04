class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        astack=[]
        for i in S:
            if i=='#' and not astack:
                continue
            if i=='#':
                astack.pop()
                continue
            astack.append(i)
        bstack=[]
        for i in T:
            if i=='#' and not bstack:
                continue
            if i=='#':
                bstack.pop()
                continue
            bstack.append(i)
        return astack==bstack


class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)

class Solution3(object):
    def backspaceCompare(self, S, T):
        import itertools
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1#用于跳过不需要的字符
                elif skip:
                    skip -= 1
                else:
                    yield x
        for x,y in itertools.zip_longest(F(S),F(T)):
            print(x,y)
        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))



k=Solution3()
print(k.backspaceCompare(S = "ab#c", T = "ad#c"))
