from typing import List
from collections import defaultdict


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        hashmap=defaultdict(int)#长度记录
        bitnumber=lambda ch:ord(ch)-ord('a')
        for word in words:#只关心字母是否存在，不关心数量以及位置
            bitmask=0
            for ch in word:
                bitmask |= 1<<bitnumber(ch)
            hashmap[bitmask]=max(hashmap[bitmask],len(word))
        maxpro=0
        for x in hashmap:
            for y in hashmap:
                if x & y==0:
                    maxpro=max(maxpro,hashmap[x]*hashmap[y])
        return maxpro

k=Solution()
print(k.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))