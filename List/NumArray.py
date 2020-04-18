from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.array=nums
        self.size=len(nums)
        self.cunsum=[0]*(self.size+1)
        for i in range(1,self.size+1):
            self.cunsum[i]=self.cunsum[i-1]+self.array[i-1]


    def update(self, i: int, val: int) -> None:
        sub=val-self.array[i]
        self.array[i]=val
        for i in range(i,self.size+1):
            self.cunsum[i]+=sub

    def sumRange(self, i: int, j: int) -> int:
        return self.cunsum[j+1]-self.cunsum[i]



