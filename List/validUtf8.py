from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        nbyte=0
        mask1=1<<7
        mask2=1<<6
        for num in data:
            mask=1<<7
            if nbyte==0:
                while mask & num:
                    nbyte+=1
                    mask>>=1
                if nbyte==0:
                    continue
                if nbyte==1 or nbyte>4:
                    return False
            else:
                if not ((num & mask1 ) and not (num & mask2)):
                    return False
            nbyte-=1
        return nbyte==0