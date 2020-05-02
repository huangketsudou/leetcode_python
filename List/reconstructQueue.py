from typing import List


class Solution:
    #题解https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode/
    '''
    方法是贪心算法，记给出的列表中的元素为[h,k],h为高度，k为前面的人数
    考虑所有的人身高都是一样的，即h相同，那么他们的排列顺序就是按照k从小到大排列，此时每个人再列表中的索引index=k
    如[[7,1],[7,0]]-->[[7,0],[7,1]]
    当所有人不是同一高度时，该策略也可行，因为对于高的人而言，矮的人看不见，所以将这个人插入到相应的k位置就可以
    [[7,1],[6,1],[7,0]]--> [[7,0],[6,1],[7,1]]
    '''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output=[]
        for p in people:
            output.insert(p[1],p)
        return output

