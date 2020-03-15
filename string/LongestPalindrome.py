class Solution:
#文章参考-小灰算法
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        rightMax = 0
        MaxCenter = 0
        MaxLength = 0
        length = [0] * len(s)
        for i in range(1, len(s) - 1):
            if i >= rightMax:
                length[i] = self.find(s, i, 0)
                rightMax = MaxCenter + length[i]
                if length[i] > MaxLength:
                    MaxLength = length[i]
                    MaxCenter = i
            else:
                #通过maxcenter找到右边的点i的最长回文长度
                LeftI = 2 * MaxCenter - i
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



class Solution:
#中心扩展法
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        start = end = 0
        n = len(s)
        for i in range(len(s)):
            len1 = self.findlength(s, i, i, n)
            len2 = self.findlength(s, i, i + 1, n)
            length=max(len1,len2)
            if length>(end-start+1):
                start=i-(length-1)//2
                end=i+length//2
        return s[start:end+1]

    def findlength(self, s, left, right, L):

        while left >= 0 and right < L and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
