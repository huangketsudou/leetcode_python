class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1=sorted(list(s1))
        l2=sorted(list(s2))
        n=len(l1)
        find=[]
        for i in range(n):
            if l1[i]>l2[i]:
                find.append(True)
            elif l1[i]<l2[i]:
                find.append(False)
            else:
                pass
        if any(find):
            return all(find)
        return True

k=Solution()
print(k.checkIfCanBreak('xya','abc'))