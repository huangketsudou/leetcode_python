from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':return '0'
        num1=num1[::-1]
        num2=num2[::-1]
        n1=len(num1)
        n2=len(num2)
        if n1<n2:
            num1,num2=num2,num1
            n1,n2=n2,n1
        res='0'
        for i,digit in enumerate(num2):
            tmp=self.stringmuldigit(num1,int(digit))+'0'*i
            res=self.StringPlusString(res,tmp)
        return res


    def stringmuldigit(self,string,n):
        res=[]
        for i,char in enumerate(string):
            num=int(char)
            res.append(num*n)
        res=self.CarrySolver(res)
        res=res[::-1]
        return ''.join(str(x) for x in res)


    def CarrySolver(self,nums):
        i=0
        while i<len(nums):
            if nums[i]>=10:
                carrier=nums[i]//10
                if i==len(nums)-1:
                    nums.append(carrier)
                else:
                    nums[i+1]+=carrier
                nums[i]&=10
            i+=1
        return nums

    def StringPlusString(self, s1, s2):
        # 这个函数的功能是：计算两个字符串的和。
        # 举例：输入为“123”， “456”, 返回为"579"
        # PS：LeetCode415题就是要写这个函数
        l1, l2 = len(s1), len(s2)
        if l1 < l2:
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        s1 = [int(x) for x in s1]
        s2 = [int(x) for x in s2]
        s1, s2 = s1[::-1], s2[::-1]
        for i, digit in enumerate(s2):
            s1[i] += s2[i]
        s1 = self.CarrySolver(s1)
        s1 = s1[::-1]
        return "".join(str(x) for x in s1)


class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = list(map(lambda i: ord(i) - ord('0'), num1))
        num2 = list(map(lambda i: ord(i) - ord('0'), num2))
        l1, l2 = len(num1), len(num2)
        res = [0 for i in range(l1 + l2 - 1)]

        for i in range(l1):
            for j in range(l2):
                res[i + j] += num1[i] * num2[j]

        for i in range(1, len(res))[::-1]:
            res[i - 1] += res[i] // 10
            res[i] = res[i] % 10

        return ''.join(map(str, res))

k=Solution()
print(k.multiply('2','3'))
