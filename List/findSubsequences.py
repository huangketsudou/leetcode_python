from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2: return []
        ans=set()
        for i in range(n):
            self.dfs([nums[i]],ans,nums,i+1,n)
        return list(map(list,ans))


    def dfs(self,array,ans,nums,idx,L):

        for j in range(idx,L):
            if nums[j]>=array[-1]:
                array.append(nums[j])
                ans.add(tuple(array))
                self.dfs(array,ans,nums,j+1,L)
                array.pop()
        return


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        #用dict过滤掉重复的元素
        def _dfs(start, temp):
            dic = {}
            if len(temp) > 1:
                res.append(temp)

            for i in range(start, len(nums)):
                if dic.get(nums[i], 0):
                    continue

                if len(temp) == 0 or nums[i] >= temp[-1]:
                    dic[nums[i]] = 1
                    _dfs(i + 1, temp + [nums[i]])

        _dfs(0, [])
        return res

k=Solution()
print(k.findSubsequences([4,6,7,7]))