class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        string = "{:0"+str(k)+"b}"
        for i in range(2**k):
            print(i)
            print(string.format(i))
            if string.format(i) not in s:
                return False
        return True


class Solution(object):
    #一共有2**k种子串
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        contains = set()
        N = len(s)
        for i in range(N - k + 1):
            contains.add(s[i:i + k])
        return len(contains) == (2 ** k)

k = Solution()
print(k.hasAllCodes("00110110",3))