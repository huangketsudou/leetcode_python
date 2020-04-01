class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        tree=['']
        for i in S:
            if i.isdigit():
                tmp=[i]
            else:
                tmp=[i.lower(),i.upper()]
            k=[]
            for j in tree:
                for n in tmp:
                    k.append(j+n)
            tree=k
        return tree


class Solution4(object):
    def letterCasePermutation(self, S):
        #笛卡尔积
        import itertools
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        print(*map(f, S))
        return map("".join, itertools.product(*map(f, S)))




k=Solution4()
print(k.letterCasePermutation('a123s'))
