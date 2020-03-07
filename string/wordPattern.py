class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str=str.split(' ')
        return list(map(pattern.index,pattern))==list(map(str.index,str))

