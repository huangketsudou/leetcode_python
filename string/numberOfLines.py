class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        n=len(S)
        cumsum=[0]*n
        prev=0
        for i in range(n):
            cumsum[i]=prev+widths[ord(S[i])-ord('a')]
            prev=cumsum[i]
        used=0
        ans=0
        for i in range(n):
            if cumsum[i]-used>100:
                ans+=1
                used=cumsum[i-1]
        return [ans+1,cumsum[-1]-used]
    
    
class Solution(object):
    def numberOfLines(self, widths, S):
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width


k=Solution()
# widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "abcdefghijklmnopqrstuvwxyz"
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
print(k.numberOfLines(widths,S))
