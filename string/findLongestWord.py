from typing import List
from collections import Counter


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for string in d:
            if self.issubsequence(s,string):
                return string
        return ''

    def issubsequence(self, str1, str2):
        i = 0
        for j in range(len(str1)):
            if str1[j] == str2[i]:
                i += 1
            if i == len(str2):
                return True
        return False
