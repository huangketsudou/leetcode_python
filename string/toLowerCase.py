class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(c)+32) if ord(c)>=65 and ord(c)<=90 else c for c in str])

