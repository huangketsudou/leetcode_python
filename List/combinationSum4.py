from typing import List



'''
背包问题的特征：给定一个target，target可以是数字也可以是字符串，在给定另一个数组nums，利用数组中的元素能都构成target
基本公式技巧：
组合公式：dp[i]+=dp[i-1]
True,False:dp[i]=dp[i] or dp[i-num]
最大最小：dp[i]=min(dp[i],dp[i-num]+1) or dp[i]=max(dp[i],dp[i-num]+1)
技巧：
1)0-1背包问题：数组中的元素不可以重复使用，此时将nums放在外循环，target放在内循环，且内循环倒序
for num in nums:
    for i in range(target,-1,-1):
2)完全背包问题，数组中的元素可以重复利用，此时将nums放在外循环，target放在内循环，且内循环正序
for num in nums:
    for i in range(1,target+1):
3)完全背包问题，数组中元素可重复利用，且需要考虑元素组成时的顺序，此时将nums放在内循环，target放在外循环，且外循环正序
for i in range(1,target+1):
    for num in nums:
注：2和3的区别可以看下面的第二解和第三解，第二解考虑了元素的组合顺序，但第三解只考虑了组合，不同的顺序视为同一顺序


'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=0
        for num in nums:
            res+=self.core(target-num,nums)
        return res


    def core(self,number,array):
        if number==0:return 1
        if number<0:return 0
        ans=0
        for num in array:
            ans+=self.core(number-num,array)
        return ans


class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        这里为什么能够考虑到顺序性?解释如下，考虑target和nums=[1,2,3]
        实际上在考虑target这个目标的组合数时，在他之前计算了target-3这个数的组合情况，把target-3记作tmp，
        而target可以通过tmp+2+1和tmp+1+2计算得来，而tmp+2与tmp+1都在计算target之前就被计算过，因此
        :param nums:
        :param target:
        :return:
        '''
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

class Solution3:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)

        for num in nums:
            for i in range(1,target+1):
                if i-num>=0:
                    dp[i]=1+dp[i-num]
        return dp[-1]