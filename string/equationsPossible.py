from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        for equation in equations:
            if equation[1] == '=':
                self.union(parent, ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a'))
        for equation in equations:
            if equation[1] == '!':
                if self.find(parent, ord(equation[0]) - ord('a')) == self.find(parent, ord(equation[3]) - ord('a')):
                    return False
        return True

    def find(self, parent, i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(self, parent, x, y):
        parent[self.find(parent, x)] = parent[self.find(parent, y)]
