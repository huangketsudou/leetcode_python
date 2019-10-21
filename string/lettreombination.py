from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        symbol={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        if len(digits)==0:
            return []
        answer=['']
        for i in digits:
            tmp=[]
            nextdigit=symbol.get(int(i))
            while len(answer)!=0:
                pre=answer.pop(0)
                for j in nextdigit:
                    tmp.append(pre+j)
            answer.extend(tmp)

        return answer


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        symbol = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        answer=[]
        for i in digits:
            tmp=[]
            for j in symbol.get(int(i)):
                if not answer:
                    tmp.append(j)
                else:
                    for pre in answer:
                        tmp.append(pre+j)
            answer=tmp
        return answer

k=Solution2()
print(k.letterCombinations('23'))
