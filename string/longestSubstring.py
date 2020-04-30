class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import defaultdict
        if not s: return 0
        n = len(s)
        max_num = len(set(s))

        # 当不同字符个数为num，最长字符为多少
        def cal(num):
            #
            left = 0
            # 目前不同字符的个数
            cur = 0
            # 大于等于k字符的个数
            ge_k = 0
            # 记录字符个数
            c = defaultdict(int)
            # 最长字符串
            res = 0
            for right in range(n):
                c[s[right]] += 1
                # 不同字符个数
                if c[s[right]] == 1:
                    cur += 1
                # 大于等于k个数
                if c[s[right]] == k:
                    ge_k += 1
                # 当字符串不同个数大于 num
                while cur > num:
                    if c[s[left]] == 1:
                        cur -= 1
                    if c[s[left]] == k:
                        ge_k -= 1
                    c[s[left]] -= 1
                    left += 1
                if ge_k == num:
                    res = max(res, right - left + 1)
            return res

        return max(cal(num) for num in range(1, max_num + 1))

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #当一个字符串中出现次数最少的字符的次数大于k时，最大的长度就是字符串的长度
        if len(s) < k:
            return 0
        # 找个字符串个数最少的字符
        t = min(set(s), key=s.count)
        # 最少字符的个数都大于等于k
        if s.count(t) >= k:
            return len(s)
        return max(self.longestSubstring(a,k) for a in s.split(t))


k=Solution()
print(k.longestSubstring("ababbc",2))