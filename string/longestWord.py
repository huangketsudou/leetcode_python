class Solution(object):

    #字典序指的是字母的自然排列顺序
    def longestWord(self, words):
        import collections
        from functools import reduce
        Trie = lambda: collections.defaultdict(Trie) #把自己当作自己元素的类型
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = list(trie.values())
        print(stack)
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans


class Solution(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word

        return ans



k=Solution()
print(k.longestWord(words = ["w","wo","wor","worl", "world"]))
