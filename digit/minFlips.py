class Solution:
    def minFlips(self, target: str) -> int:
        prev = '0'
        count = 0
        for c in target:
            if c != prev:
                count+=1
                prev = c
        return count


k=Solution()
print(k.minFlips("001011101"))