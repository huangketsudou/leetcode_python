from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        def dfs(s, t) -> float:
            if s not in graph:  # 起点不在表中
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)  # 防止双向表重复加入
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1  # 目标不在表中

        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res


class Solution:
    #四边形并查表
    '''
    思考这样的一个构造过程，
    a->b
    c->d
    对于这样一个构成的情况，如果还有b->d,那么b与d之间连接并赋权v，
    如果b->c,那么此时c的父节点为d，c对d的权为w，把b的父节点记为d，b对d的权为w*v，此时a的父节点为b，
    下次查找a时，就会把a的父节点修改为d，并给与新的权w*v*k，k是a对b的权
    如果a->c,a对b的权为k，c对d权为w，a对c的权为v,那么a对d的权为w*v/k
    '''
    def union(self, p, q, cur):
        rootp = self.find(p)
        rootq = self.find(q)

        self.parents[rootp] = rootq
        self.weight[rootp] = self.weight[q] * cur / self.weight[p]

    def find(self, p):#并查集要找到他的祖宗节点
        tmpp = p
        ans = 1.0
        while (p != self.parents[p]):
            ans *= self.weight[p]
            p = self.parents[p]
        self.parents[tmpp] = p
        self.weight[tmpp] = ans
        return p

    def calcEquation(self, equations, values, queries):

        n = len(equations)
        self.parents = [i for i in range(999)]
        self.weight = [1.0 for i in range(999)]#存储节点与其祖宗的比值
        self.datas = {}

        num = 1
        for i in range(n):
            s1 = equations[i][0]
            if s1 not in self.datas:
                self.datas[s1] = num
                num += 1
            s2 = equations[i][1]
            if s2 not in self.datas:
                self.datas[s2] = num
                num += 1
            self.union(self.datas[s1], self.datas[s2], values[i])#带权的并查表
        res = []
        for i in range(len(queries)):

            s1 = queries[i][0]
            s2 = queries[i][1]
            if s1 not in self.datas or s2 not in self.datas:#不存在的数
                res.append(-1.0)
                continue
            rootp = self.find(self.datas[s1])
            rootq = self.find(self.datas[s2])
            # print(rootp,rootq)
            if rootp != rootq:#无法求解的数，没有共同的祖先节点
                res.append(-1.0)
                continue
            res.append(self.weight[self.datas[s1]] / self.weight[self.datas[s2]])
        return res