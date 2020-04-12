class Solution2:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        ans = []
        for que in queries:
            ans.append(P.index(que))
            P.remove(que)
            P = [que] + P
        return ans
