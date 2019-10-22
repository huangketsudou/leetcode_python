from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        tmp=''
        self.recur(n,answer,tmp,n)
        return answer


    def recur(self,n,answer,tmp,right):
        if n==0:
            tmp+=')'*right
            answer.append(tmp)
        else:
            self.recur(n-1,answer,tmp+'(',right)
            if right>n:
                self.recur(n,answer,tmp+')',right-1)


k=Solution()
print(set(k.generateParenthesis(4)))
