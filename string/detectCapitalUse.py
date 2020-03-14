class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word or word.lower() == word: return True
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]: return True
        return False


class Solution2:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()




k=Solution()
print(k.detectCapitalUse('LEetcode'))
