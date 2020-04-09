class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left,right=0,len(S)-1
        ans=list(S)
        while left<right:
            while left<right and not S[left].isalpha():
                left+=1
            while right>left and not S[right].isalpha():
                right-=1
            ans[left],ans[right]=ans[right],ans[left]
            left+=1
            right-=1
        return ''.join(ans)


k=Solution()
print(k.reverseOnlyLetters("ab-cd"))
