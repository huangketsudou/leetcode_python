from collections import deque


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        node=preorder.split(',')
        n=len(node)
        stack=deque()
        i=0
        if node[i]!='#':stack.append([i,0])
        while stack:
            i+=1
            if i>=n:break #不构成完整的树1,#这种
            if node[i]!='#':
                stack.append([i,0])
            else:
                stack[-1][1]+=1
                while stack and stack[-1][1]==2:
                    stack.pop()
                    if stack:#保证最后只剩一节点时能过
                        stack[-1][1]+=1
        return i==n-1


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # number of available slots，合法可用的点
        slots = 1

        for node in preorder.split(','):
            # one node takes one slot
            slots -= 1

            # no more slots available
            if slots < 0:
                return False

            # non-empty node creates two children slots
            if node != '#':
                slots += 2

        # all slots should be used up
        return slots == 0


