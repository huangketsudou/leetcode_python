class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        B=len(s)
        rightMax = MaxCenter=MaxLength=0
        length = [0] * B
        for i in range(1,B - 1):
            if i >= rightMax:
                length[i] = self.find(s, i, 0)
                rightMax = MaxCenter + length[i]
                if length[i] > MaxLength:
                    MaxLength = length[i]
                    MaxCenter = i
            else:
                LeftI = 2 * MaxCenter - i#对称点
                if i + length[LeftI] < rightMax:
                    length[i] = length[LeftI]
                else:
                    length[i] = self.find(s, i, length[LeftI])
                    rightMax = MaxCenter + length[i]
                    if length[i] > MaxLength:
                        MaxLength = length[i]
                        MaxCenter = i
        answer=s[MaxCenter-MaxLength:MaxCenter+MaxLength+1]
        answer=answer.replace('#','')
        return answer

    def find(self, s, center, length):
        while center - length - 1 >= 0 and center + length + 1 < len(s) and s[center - length - 1] == s[
            center + length + 1]:
            length += 1
        return length

k=Solution()
print(k.longestPalindrome('abba'))
