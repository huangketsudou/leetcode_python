class Solution4:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        n = len(words)
        ans = []
        for i, word in enumerate(words):
            j = n - 1
            while i < j:
                if words[j].find(word) != -1:
                    ans.append(word)
                    break
                j -= 1
        return ans


k = Solution4()
print(k.stringMatching(words=["leetcode", "et", "code"]))
