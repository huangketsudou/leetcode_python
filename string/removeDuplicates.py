

class Solution:
    def removeDuplicates(self, S: str) -> str:
        char=[]
        for c in S:
            if not char or c!=char[-1]:
                char.append(c)
            else:
                char.pop()
        return ''.join(char)
