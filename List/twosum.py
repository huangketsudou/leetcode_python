class Solution:
    def twosum(self,nums,target):
        substract={}
        for index,i in enumerate(nums):
            sub=target-i
            if sub in substract:
                return [substract[sub],index]
            substract[i]=index
        return None

c=Solution()

print(c.twosum([2,7,11,15],9))


class Solution2:
    def twoSum(self,nums,target):
        id=sorted(range(len(nums)),key=lambda k:nums[k])
        small=0
        big=len(nums)-1
        while small<big:
            tmp=nums[id[small]]+nums[id[big]]
            if target==tmp:
                return [id[small],id[big]]
            if target>tmp:
                small+=1
            if target<tmp:
                big-=1
        return None

k=Solution2()
print(k.twoSum([2,7,11,15],9))
