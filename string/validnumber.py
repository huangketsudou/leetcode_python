from typing import List


class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip(' ')
        evalid=True
        dotvalid=True
        n=len(s)
        if n==0:return False
        for i in range(n):
            if i==0 and s[i]=='e':return False
            if evalid and s[i]=='e':
                if i==n-1:return False
                if s[i-1] not in '0123456789.':return False
                evalid=False
                dotvalid=False
            elif dotvalid and s[i]=='.':
                if (i==n-1 and s[i-1] not in '0123456789') or (i==0 and s[i+1] not in '0123456789') or \
                        (s[i-1] not in '0123456789' and s[i+1] not in '0123456789'):return False
                dotvalid=False
            elif s[i] in '+-' and (i == 0 or s[i - 1] in 'Ee') and i<n-1:
                continue
            elif s[i] not  in '0123456789':
                return False
        return True


class Solution2:
    def isNumber(self,s):
        s=s.strip(' ')
        numeric,start=self.scaninterger(s,0)
        if s[start]=='.':
            start+=1
            numeric,start=self.scanunsignedinterger(s,start) or numeric
        if s[start]=='e':
            start+=1
            tmp,start=self.scaninterger(s,start)
            numeric=numeric and tmp
        return numeric and start==len(s)


    def scaninterger(self,s,start):
        if s[start] in '+-':
            start+=1
        return self.scanunsignedinterger(s,start)


    def scanunsignedinterger(self,s,start):
        before=start
        while start<len(s) and s[start] in '0123456789':
            start+=1
        return start>before,start


class Solution3:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        state = 0
        s = list(s)
        for i in s:
            if state == 0:
                if i == '.':
                    state = 8
                elif '0' <= i <= '9':
                    state = 1
                elif i == '+' or i == '-':
                    state = 7
                else:
                    return False
            elif state == 1:
                if '0' <= i <= '9':
                    state = 1
                elif i == 'e' or i == 'E':
                    state = 4
                elif i == '.':
                    state = 2
                else:
                    return False
            elif state == 2:
                if '0' <= i <= '9':
                    state = 3
                elif i == 'e' or i == 'E':
                    state = 4
                else:
                    return False
            elif state == 3:
                if '0' <= i <= '9':
                    state = 3
                elif i == 'e' or i == 'E':
                    state = 4
                else:
                    return False
            elif state == 4:
                #e后只能有符号以及整数
                if '0' <= i <= '9':
                    state = 6
                elif i == '+' or i == '-':
                    state = 5
                else:
                    return False
            elif state == 5:
                if '0' <= i <= '9':
                    state = 6
                else:
                    return False
            elif state == 6:
                #这个是针对e的指数部分的数值部分
                if '0' <= i <= '9':
                    state = 6
                else:
                    return False
            elif state == 7:
                if '0' <= i <= '9':
                    state = 1
                elif i == '.':
                    state = 8
                else:
                    return False
            elif state == 8:
                if '0' <= i <= '9':
                    state = 3
                else:
                    return False
        #return的表达为1表示整数结尾，2小数点结尾，3表示小数部分结尾，6表示科学计数法结尾
        return state in [1, 2, 3, 6]


k=Solution3()
print(k.isNumber('+1.1e1e3'))

