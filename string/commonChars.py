from typing import List
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        c=None
        for word in A:
            if c is None:
                c=Counter(word)
            else:
                c = c & Counter(word)
        ans=[]
        for k,v in c.items():
            tmp=list(k*v)
            ans.extend(tmp)
        return ans


k=Solution()
print(k.commonChars(["bella","label","roller"]))