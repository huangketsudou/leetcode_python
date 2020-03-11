class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n=len(A)
        if n<3:return False
        summary=sum(A)
        if summary % 3!=0:return False
        part=summary//3
        res=0
        cumsum=0
        for i in A:
            cumsum+=i
            if cumsum==(res+1)*part:
                res+=1
            if res==3:
                break
        return res==3
    
