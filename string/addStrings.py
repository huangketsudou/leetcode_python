class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)>len(num2):
            n1=num1[::-1]
            n2=num2[::-1]
        else:
            n1=num2[::-1]
            n2=num1[::-1]
        res=''
        l1=len(n1)
        l2=len(n2)
        carry=0
        for i in range(l2):
            summary=int(n1[i])+int(n2[i])+carry
            res+=str(summary % 10)
            carry=summary//10

        for j in range(l2,l1):
            summary=int(n1[j])+carry
            res += str(summary % 10)
            carry = summary // 10
        if carry:
            res+='1'
        return res[::-1]


class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            n1 = num1[i] if i >= 0 else '0'
            n2 = num2[j] if j >= 0 else '0'
            temp = ord(n1) + ord(n2) - 2 * ord('0') + carry
            cur = temp % 10
            carry = temp // 10
            res = chr(cur + 48) + res
            i -= 1
            j -= 1
        return '1' + res if carry != 0 else res





k=Solution()
print(k.addStrings('5','408'))
