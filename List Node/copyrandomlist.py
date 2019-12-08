from typing import List


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        hashmap = {}
        cursor = head
        while cursor:
            if cursor in hashmap:
                node = hashmap[cursor]
            else:
                node = Node(cursor.val, None, None)
                hashmap[cursor] = node
            if cursor.next in hashmap:
                node.next = hashmap[cursor.next]
            else:
                if  cursor.next:
                    node.next = Node(cursor.next.val,None,None)
                    hashmap[cursor.next]=node.next
            if cursor.random in hashmap:
                node.random = hashmap[cursor.random]
            else:
                if cursor.random:
                    node.random = Node(cursor.random.val,None,None)
                    hashmap[cursor.random] = node.random
            cursor = cursor.next
        return hashmap[head]



class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:return head
        cursor=head
        while cursor:
            newnode=Node(cursor.val,None,None)
            newnode.next = cursor.next
            cursor.next=newnode
            cursor=newnode.next
        cursor=head
        while cursor:
            new=cursor.next
            new.random = cursor.random.next if cursor.random else None
            cursor=new.next
        oldnode=head
        cloned=head.next
        clone=head.next
        while oldnode:
            oldnode.next = cloned.next
            cloned.next = oldnode.next.next if oldnode.next else None
            oldnode=oldnode.next
            cloned=cloned.next
        return clone










N1=Node(1,None,None)
N2=Node(2,None,None)
N3=Node(3,None,None)
N4=Node(4,None,None)
N1.next=N2
N2.next=N3
N3.next=N4
N1.random=N2
N2.random=N2
N3.random=N1



k=Solution2()
g=k.copyRandomList(N1)


while g:
    print(g.val)
    if g.random:
        print(g.random.val)
    g=g.next

