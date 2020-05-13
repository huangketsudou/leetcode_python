from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        item=list(c.items())
        item.sort(key=lambda x:x[1],reverse=True)
        ans=''
        for k,v in item:
            ans+=k*v
        return ans

k=Solution()
print(k.frequencySort('Aabb'))