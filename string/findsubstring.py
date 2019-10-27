from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        amount=len(words)
        perlength=len(words[0])
        length=len(s)
        if length<perlength:
            return []
        table=defaultdict(int)
        for i in words:
            table[i]+=1
        result=[]
        for i in range(0,perlength):
            curnum=0
            left=right=i
            curdict=defaultdict(int)
            while right+perlength<=length:
                word=s[right:right+perlength]
                right+=perlength
                if word not in words:
                    left=right
                    curdict.clear()
                    curnum=0
                else:
                    curdict[word]+=1
                    curnum+=1
                    while curdict[word]>table[word]:
                        leftword=s[left:left+perlength]
                        left+=perlength
                        curdict[leftword]-=1
                        curnum-=1
                    if curnum==amount:
                        result.append(left)
        return result


k=Solution()
print(k.findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"]))
