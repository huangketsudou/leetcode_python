class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        known = Counter(chars)
        res = 0
        for word in words:
            w = Counter(word)
            flag = True
            for k, v in w.items():
                if k not in known or v > known[k]:
                    flag = False
            if flag:
                res += sum(w.values())
        return res


class Solution2:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans




k=Solution()
print(k.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
