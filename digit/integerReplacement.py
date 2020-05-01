class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1: return 0
        if n & 1:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        else:
            return 1 + self.integerReplacement(n // 2)


class Solution:
    #观察数字n:如果二进制表示为xxx11，那么为了让他消去尽可能多的1，最好的方法是加1
    #观察数字n:如果二进制表示为xxx01，那么最好的消去1的方法是减去1，
    #特殊情况，对于数字3，3->4->2->1比3->2->1的次数多，该情况要减1
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n & 1:
                n+=-1 if n & 2 ==0 or n==3 else 1
            else:
                n >>= 1
            count+=1
        return count