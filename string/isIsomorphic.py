class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping=zip(s,t)
        dictionary={}
        for k,v in mapping:
            r=dictionary.setdefault(k,v)
            if r!=v:return False
        mapping=zip(t,s)
        dictionary={}
        for k,v in mapping:
            r = dictionary.setdefault(k, v)
            if r != v:
                return False
        return True

class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #映射到其索引上
        #map函数映射，只会返回最小的索引值
        return [*map(s.index, s)] == [*map(t.index, t)]




k=Solution()
print(k.isIsomorphic('foo','bar'))
