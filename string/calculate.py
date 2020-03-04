from typing import List

#---------------------------------
只有加减，带括号
class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        forlumn = s.replace(' ','')
        n=len(forlumn)
        return self.compute(0,n,forlumn)

    def compute(self, idx, n, forlumn):
        bool=1
        result=0
        i=idx
        while i<n:
            if forlumn[i] == '+':
                bool = 1
                i += 1
            elif forlumn[i] == '-':
                bool = -1
                i += 1
            elif forlumn[i]=='(':

                tmp,i=self.compute(i+1,n,forlumn)
                result+=tmp*bool
            elif forlumn[i]==')':
                return result,i+1
            else:
                tmp = 0
                while i < n and forlumn[i] in '0123456789':
                    tmp = 10 * tmp + int(forlumn[i])
                    i += 1
                result += bool * tmp

        return result

def compute(s,idx):
    bool = 1
    result = 0
    i = idx
    n = len(s)
    while i < n:
        if s[i] == '+':
            bool = 1
            i += 1
        elif s[i] == '-':
            bool = -1
            i += 1
        elif s[i]=='(':
            tmp,i=compute(s,i+1)
            result+=tmp*bool
        elif s[i]==')':
            return result,i+1
        else:
            tmp = 0
            while i < n and s[i] in '0123456789':
                tmp = 10 * tmp + int(s[i])
                i += 1
            result += bool * tmp


    return result


class Solution2:
    def calculate(self, s: str) -> int:
        operand=0
        sign=1
        result=0
        stack=[]
        for i in s:
            if i.isdigit():
                operand=10*operand+int(i)
            elif i=='+':
                result+=operand*sign
                sign=1
                operand=0
            elif i=='-':
                result+=operand*sign
                sign=-1
                operand=0
            elif i=='(':
                stack.append(result)
                stack.append(sign)
                sign=1
                result=0
            elif i==')':
                result+=sign*operand
                result*=stack.pop()
                result+=stack.pop()
                operand=0
        return result+sign*operand

k=Solution()
print(k.calculate("(1+(4+5+2)-3)+(6+8)"))
print(compute("(1+(4+5+2)-3)+(6+8)",0))

#加减乘除，不带括号


from typing import List
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        operand = 0
        sign = '+'
        stack = []
        for i, v in enumerate(s):
            if v.isdigit():
                operand = operand * 10 + int(v)
            if v in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(operand)

                elif sign == '-':
                    stack.append(-operand)

                elif sign == '*':
                    stack.append(stack.pop() * operand)

                elif sign == '/':
                    if stack[-1]<0:
                        stack.append(-(-stack.pop()//operand))
                    else:
                        stack.append(stack.pop() // operand)

                sign = v
                operand = 0
        return sum(stack)


k = Solution()
print(k.calculate("14-3/2"))


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operaters = {
            '+':lambda x : stack.append(x),
            '-':lambda x : stack.append(-x),
            '*':lambda x : stack.append(x*stack.pop()),
            '/':lambda x : stack.append(int(stack.pop()/x)),
        }
        num = 0
        last_op = '+'
        for c in s + 'e':# 结束符，把最后一个数字和字符结合起来
            if c.isdigit():
                num = num*10+int(c)
            elif c != ' ': # 遇到下一个符号，上一个符号和上一个数字结算
                res = operaters[last_op](num)
                num = 0
                last_op = c
        return sum(stack)
