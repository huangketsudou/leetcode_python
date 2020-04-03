class Solution:
    def toGoatLatin(self, S: str) -> str:
        words=S.split(' ')
        result=[]
        for i,word in enumerate(words):
            if word[0] not in 'aiueoAIUEO':
                word=word[1:]+word[0]
            word=word+'ma'+'a'*(i+1)
            result.append(word)
        return ' '.join(result)



class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        for i, w in enumerate(S.split(" ")):
            if w[0] in "aeiouAEIOU":
                res.append(w + "ma" + "a" * (i+1))
            else:
                res.append(w[1:] + w[0] + "ma" + "a" * (i+1))
        return " ".join(res)

k=Solution()
print(k.toGoatLatin("I speak Goat Latin"))
