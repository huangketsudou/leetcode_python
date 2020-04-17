from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #桶排序用于不关系最后的排序结果，而只关心组间差异的情况
        #注意，桶排序中会限定数组中元素的范围
        bucket = [0] * 101
        for i in heights:
            bucket[i] += 1
        count = 0
        j = 0
        for i in range(101):
            while bucket[i] > 0:
                if heights[j] != i:
                    count += 1
                    j += 1
                    bucket-=1
        return count


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedheight=sorted(heights)
        count=0
        for i,v in enumerate(heights):
            if v!=sortedheight[i]:
                count+=1
        return count