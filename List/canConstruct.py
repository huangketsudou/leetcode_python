class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        a=Counter(ransomNote)
        b=Counter(magazine)

        for k,v in a.items():
            if k not in b or v>b[k]:
                return False
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)

