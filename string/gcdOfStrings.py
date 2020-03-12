class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not (str1 and str2): return ''
        n1 = len(str1)
        n2 = len(str2)
        if n1 < n2:
            str1, str2 = str2, str1
            n1, n2 = n2, n1
        res=''
        for i in range(1, n2 + 1):
            if n2 % i != 0 or n1 % i != 0: continue
            tmpgcd = str2[:i]
            if tmpgcd*(n2//i)==str2 and tmpgcd*(n1//i)==str1:
                res=tmpgcd

        return res


class Solution2:
    #逆序查找，更快
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        for i in range(min(l1, l2), 0, -1):
            if l1 % i == 0 and l2 % i == 0:
                if str1[:i] * (l1 // i) == str1 and str1[:i] * (l2 // i) == str2:
                    return str1[:i]
        return ""


k=Solution()
print(k.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
