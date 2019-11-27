from typing import List



class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return root
        stack=[root]

        while stack:
            tmp=[]
            while stack:
                head=stack.pop(0)
                if stack:
                    head.next=stack[0]
                if head.left:
                    tmp.append(head.left)
                if head.right:
                    tmp.append(head.right)
            stack=tmp
        return root


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        pre=root
        while pre:
            cur=pre
            while cur:
                if cur.left:cur.left.next=cur.right
                if cur.right and cur.next:cur.right.next=cur.next.left
                cur=cur.next
            pre=pre.left
        return root


t1=Node(1)
t2=Node(2)
t3=Node(3)
t1.left=t2
t1.right=t3
t4=Node(4)
t5=Node(5)
t6=Node(6)
t7=Node(7)
t2.left=t4
t2.right=t5
t3.left=t6
t3.right=t7


k=Solution2()
a=k.connect(t1)


print(a.left.next.val)
