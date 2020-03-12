class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        end = 1

        while end <= n // 2:
            if n % end == 0:
                tmpstr = s[:end]
                if tmpstr * (n // end) == s: return True
            end += 1
        return False

