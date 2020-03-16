class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s: return
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
            
class Solution:
    def reverseString(self, s):
        s.reverse()

        

class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
class Solution:
    def reverseWords(self, s: str) -> str:

        l=s.split(' ')
        rl=list(map(lambda x:x[::-1],l))
        return ' '.join(rl)


k=Solution()
print(k.reverseWords("Let's take LeetCode contest"))



class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1])[::-1]

