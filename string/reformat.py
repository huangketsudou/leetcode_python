class Solution:
    def reformat(self, s: str) -> str:
        number=[]
        char=[]
        n=len(s)
        for c in s:
            if c.isdigit():
                number.append(c)
            else:
                char.append(c)
        if abs(len(char)-len(number))>1:
            return ''
        choose=[number,char]
        id=0
        if len(number)<len(char):
            id=1
        i=0
        ans=''
        while i<n:
            ans+=choose[id].pop(0)
            id=1-id
            i+=1
        return ans
