from typing import List
from collections import defaultdict


'''
对于一条有向通路而言，只需要按着路线走就可以，但是在路线具有环路的情况下，就有可能没走完路线就出去了
为此按照字典序排列之后，一直走，当走到末尾时，就可以加入路线数组中，因为他是最后的孤岛，因此出现在最后
参考https://leetcode-cn.com/problems/reconstruct-itinerary/solution/javadfsjie-fa-by-pwrliang/

'''


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        MAP=defaultdict(list)
        for start,end in tickets:
            MAP[start].append(end)
        for key in MAP.keys():
            MAP[key].sort(reverse=True)
        ans=[]
        stack=["JFK"]
        while stack:
            node=stack[-1]
            if MAP[node]:
                stack.append(MAP[node].pop())#还有路可以走
            else:
                ans.append(stack.pop())#没路了

        return ans[::-1]



class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)   #邻接表
        for f, t in tickets:
            d[f] += [t]         #路径存进邻接表
        for f in d:
            d[f].sort()         #邻接表排序
        ans = []
        def dfs(f):             #深搜函数
            while d[f]:
                dfs(d[f].pop(0))#路径检索
            ans.insert(0, f)    #放在最前
        dfs('JFK')
        return ans

