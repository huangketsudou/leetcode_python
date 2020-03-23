class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)
        common = set1 & set2
        res = float('inf')
        ans = []
        for h in common:
            dres=list1.index(h)+list2.index(h)
            if dres< res:
                ans = [h]
                res = dres
            elif dres == res:
                ans.append(h)
        return ans
