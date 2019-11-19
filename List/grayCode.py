from typing import List


class Solution:
    # 下一阶格雷码由上一阶格雷码得到
    # 注意格雷码的对称形式：000，010，011，001  |  101 111 110 100 ,后面的两位成镜像对称
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res


class Solution2:
    #维基百科格雷码生成思路
    def grayCode(self, n):
        res = [0]
        for i in range(1, 1 << n):
            prev=res[-1]
            if i%2==1:
                prev^=1
                res.append(prev)
            else:
                tmp=prev
                for j in range(n):
                    if (tmp & 1 )==1:
                        prev=prev^(1<<(j+1))
                        res.append(prev)
                        break
                    tmp=tmp>>1
        return res



class Solution3:
    #二进制转格雷码公式，最高位保留，其余为未该位二进制与其上一位的二进制的异或
    def grayCode(self,n):
        res=[]
        for i in range(1<<n):
            res.append(i ^ (i>>1))
        return res



k=Solution3()
print(k.grayCode(2))
