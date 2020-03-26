class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        c=Counter(moves)
        return c['U']==c["D"] and c['L']==c['R']
