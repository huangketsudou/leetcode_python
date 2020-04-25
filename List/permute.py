from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        n=len(nums)
        tmp=[]
        used=[]
        self.core(n,answer,nums,tmp,used)
        return answer


    def core(self,n,answer,nums,tmp,used):
        if len(used)==n:
            answer.append(tmp[:])#这里必须用列表切片实现列表的复制，不然输出的所有结果都是一样的
        for i in range(n):
            if i in used:
                continue
            tmp.append(nums[i])
            used.append(i)
            self.core(n,answer,nums,tmp,used)
            used.pop(-1)
            tmp.pop(-1)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]

        def core(tmp,seen):
            if len(tmp)==n:
                ans.append(tmp)
                return
            for i in range(n):
                if i not in seen:
                    seen.add(i)
                    core(tmp+[nums[i]],seen)
                    seen.remove(i)
        saw=set()
        core([],saw)
        return ans


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

            
k=Solution()
print(k.permute([1,2,3]))
