from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        while words:
            tmplength = 0
            tmpused: List[str] = []
            while tmplength < maxWidth and len(words):
                nextword = words[0]
                wordlength = len(nextword)
                if tmplength + wordlength <= maxWidth:
                    tmpused.append(words.pop(0))
                    tmplength += wordlength + 1
                else:
                    break
            if words and len(tmpused)!=1:
                numOfword = len(tmpused)
                sentence = tmpused.pop(0)
                sum_wordlength = tmplength - numOfword
                per_space =(maxWidth-sum_wordlength)//(numOfword-1)
                res_space=(maxWidth-sum_wordlength)%(numOfword-1)
                while tmpused:
                    if res_space:
                        sentence+=' '*per_space+' '+tmpused.pop(0)
                        res_space-=1
                    else:
                        sentence+=' '*per_space+tmpused.pop(0)
                answer.append(sentence)
            else:
                sentence=' '.join(tmpused)
                sentence+=' '*(maxWidth-len(sentence))
                answer.append(sentence)
        return answer



k=Solution()
words= ["What","must","be","acknowledgment","shall","be"]
print(k.fullJustify(words,16))
