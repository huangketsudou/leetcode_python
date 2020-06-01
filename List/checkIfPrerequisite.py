from typing import List
from collections import defaultdict

class Solution:
    '''
    这段代码是错误的，因为没有考虑到prerequisites的顺序，如下的两个例子
    prerequisites = [[3, 4], [2, 3], [1, 2], [0, 1]]和
    prerequisites = [[0,1],[1,2],[2,3],[3,4]]，queries都一样，queries = [[0,4],[4,0],[1,3],[3,0]]
    第一个返回的的结果为[False,False,False,False]
    第二个返回的结果为[True,False,True,False],第二个返回结果才是对的，因为第一个prere没有正确的将所有的parent给到其子孙上
    '''
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mapping =defaultdict(set)
        for i in range(n):
            mapping[i].add(i)
        for prev,nxt in prerequisites:
            mapping[nxt].add(prev)
            mapping[nxt]|=mapping[prev]
        print(mapping)
        ans = []
        for prev,nxt in queries:
            if prev in mapping[nxt]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


from functools import lru_cache
class Solution:
    #一定要用并查集的话用这个
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        req = defaultdict(set)
        for L,R in prerequisites:
            req[L].add(R)
        #递归调用将所有的parent给出
        @lru_cache(None)
        def recur(L):
            for R in req[L]:
                recur(R)
            for R in list(req[L]):
                req[L]|=(req[R])

        for i in range(n):
            recur(i)

        return [R in req[L] for L,R in queries]


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = [[False for j in range(n)] for i in range(n)]
        for u, v in prerequisites: #表示u是v的前置
            g[u][v] = True
        # i，j之间如果能通过k连接，那么i是j的前置
        # 注意必须先定好中间的节点k，再查看i，j能否通过k来联通
        # 如果先定好i，j，考虑一种情况，1 -> 2 -> 4 -> 3 ,那么检查1 ，3的时候无法通过一个节点正确连接，后面再检查2 3 之后也无法将1 3 连接起来
        # 但如果先检查所有能通过k连接的数据，那么能通过2连接1和4，之后再检查能通过4连接的，就能把1和3连接起来
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = g[i][j] or (g[i][k] and g[k][j])
        ans = []
        for u, v in queries:
            ans.append(g[u][v])
        return ans

class Solution(object):
    #dfs遍历法
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        self.graph = collections.defaultdict(list)
        for pre in prerequisites:
            self.graph[pre[0]].append(pre[1])
        return [self.dfs(query[0], query[1]) for query in queries]

    # start -> end ?
    @functools.lru_cache
    def dfs(self, start, end):
        if start == end:
            return True
        return any(self.dfs(nxt, end) for nxt in self.graph[start])


k=Solution()
print(k.checkIfPrerequisite(n = 5, prerequisites = [[3, 4], [2, 3], [1, 2], [0, 1]], queries = [[0,4],[4,0],[1,3],[3,0]]))