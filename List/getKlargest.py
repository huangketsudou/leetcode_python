from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import nlargest

        return nlargest(k,nums)[-1]




class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        def partition(left,right,index):
            pivot=nums[index]
            nums[index],nums[right]=nums[right],nums[index]
            store_index=left
            for i in range(left,right):
                if nums[i]<pivot:
                    nums[store_index],nums[i]=nums[i],nums[store_index]
                    store_index+=1
            nums[right],nums[store_index]=nums[store_index],nums[right]
            return store_index


        def select(left,right,k_smallest):
            if left==right:
                return nums[left]
            index=random.randint(left,right)
            index=partition(left,right,index)
            if k_smallest==index:
                return nums[k_smallest]
            elif k_smallest<index:
                return select(left,index-1,k_smallest)
            else:
                return select(index+1,right,k_smallest)


        return select(0,len(nums)-1,len(nums)-k)



k=Solution()
print(k.findKthLargest([3,2,3,1,2,4,5,5,6],4))
print(sorted([3,2,3,1,2,4,5,5,6]))
