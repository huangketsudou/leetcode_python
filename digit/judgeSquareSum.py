class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            right=int(math.sqrt(c-left*left))
            tmp = left * left + right * right
            if tmp == c:
                return True
            else:
                left += 1
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=2
        while i*i<c:
            count=0
            if c%i==0:
                while c%i==0:
                    count+=1
                    c//=i
                if i%4==3 and count%2!=0:
                    return False
            i+=1
        return c%4!=3
