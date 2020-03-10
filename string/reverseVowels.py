class Solution:
    def reverseVowels(self, s: str) -> str:
        tool = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
        l = 0
        r = len(s)-1
        s = list(s)
        while l < r:
            if s[l] not in tool:
                l += 1
                continue
            if s[r] not in tool:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
        
        

class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        vowel = 'aiueoAIUEO'
        p1, p2 = 0, len(arr) - 1
        while p1 < p2:
            while arr[p1] not in vowel and p1 < p2:
                p1 += 1
            while arr[p2] not in vowel and p1 < p2:
                p2 -= 1
            if p1 < p2:
                arr[p1], arr[p2] = arr[p2], arr[p1]
                p1 += 1
                p2 -= 1
        return ''.join(arr)

#代码写太烂了
