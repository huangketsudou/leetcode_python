class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            print(word)
            if len(word) >= len(searchWord) and word.find(searchWord) == 0:
                return i
        return -1
