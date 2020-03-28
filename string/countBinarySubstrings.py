class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2: return 0
        zero = s.count('0')
        one = n - zero
        res = 0
        for i in range(1, min(zero, one)):
            string = '0' * i + '1' * i
            res += s.count(string)
            string = '1' * i + '0' * i
            res += s.count(string)
        return res


class Solution(object):
    # 0011包含01 000111包含0011和01
    # 将字符串分为相同字符的字段，计算其长度
    def countBinarySubstrings(self, s):
        import itertools
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))


class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans


class Solution4(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, cur)
                prev ,cur= cur,1
            else:
                cur += 1
        return ans + min(prev, cur)


k = Solution4()
print(k.countBinarySubstrings("10101"))
