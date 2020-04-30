class Solution:
    def lastRemaining(self, n: int) -> int:
        count = n
        first = 1
        diff = 1
        isfromLeft = True
        #每次都去找数组的最左端的数字
        #当数字从左消除时，数组最左端数据变为first+diff的数据
        #当数字从右消除时，如果剩余的数量为偶数，first不变
        #当剩余的数量为奇数时，first变为first+diff
        while count > 1:
            if isfromLeft:
                first += diff
            else:
                if count & 1 == 1:
                    first += diff
            count >>= 1
            diff <<= 1
            isfromLeft =  not isfromLeft
        return first

class Solution2:
    def lastRemaining(self, n: int) -> int:
        #类似约瑟夫桥环，将删除数据后的数组进行重新编号,/表示被删除
        '''
        1     2     3     4 ...     2k-1    2k   原数组
        /     k     /   k-1 ...       /      1   重新编号
        如图可以看到定义编号函数f(2k)表示数组数量2k时的编号，f(k)表示数组数量k时的编号
        可以从数据中看到，f(2k)=2(k+1-f(k)),如果数组的数量为奇数，即2k+1，可以在原数组最后
        补一个2k+1,该数会被删除，所以与奇偶性无关
        :param n:
        :return:
        '''
        return 1 if n == 1 else 2 * (n // 2 + 1 - self.lastRemaining(n // 2))


class Solution3:
    #超内存了
    def lastRemaining(self, n: int) -> int:
        dp = [0] * (1 + n)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = 2 * (i // 2 + 1 - dp[i // 2])
        return dp[n]


k = Solution()
print(k.lastRemaining(12))
