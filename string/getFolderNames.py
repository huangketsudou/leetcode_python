from typing import List
from collections import defaultdict


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        folder = defaultdict(int)
        visited = set()
        result = []
        for name in names:
            if name in folder:
                newname = name
                k = folder[name]
                while newname in visited:
                    newname = name + "(" + str(k) + ")"
                    k += 1
                result.append(newname)
                folder[name] = k
                folder[newname] = 1
                visited.add(newname)
            else:
                result.append(name)
                folder[name] += 1
                visited.add(name)
        return result
