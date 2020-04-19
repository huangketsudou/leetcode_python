from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ans=[]
        tables=set()
        menus=set()
        mapping=defaultdict(list)
        for user,table,order in orders:
            tables.add(int(table))
            menus.add(order)
            mapping[int(table)].append(order)
        print(mapping)
        menus=sorted(list(menus))
        tables=sorted(list(tables))
        ans.append(["Table"]+menus)
        for num in tables:
            tmp=[str(num)]
            for v in menus:
                tmp.append(mapping[num].count(v))
            ans.append(tmp)
        return ans

k=Solution()
print(k.displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))