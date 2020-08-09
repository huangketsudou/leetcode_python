class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        j = n
        reverse = False
        while j != 1:
            if k == length // 2 + 1:
                return "1" if not reverse else '0'
            elif k <= length // 2:
                length = length // 2
            else:
                k = length - k + 1
                length = length // 2
                reverse = reverse ^ True
            j -= 1
            # print("k="+str(k))
            # print(length)
        return "1" if reverse else '0'

class Solution2:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        i = 1

        while i < n:
            cur = s + '1' + ''.join(['0' if c == '1' else '1' for c in s[::-1]])
            s = cur
            i += 1
        return s[k - 1]


k = Solution()
print(k.findKthBit(n = 4, k = 15))
